"""Zenodo PLACEHOLDER + duplicate-record audit and cleanup.

This script finds all records tagged with 'PLACEHOLDER' or 'duplicate-record'
subjects, reports them, and optionally deletes them via the Zenodo API.

Usage:
    python zenodo_cleanup.py [--dry-run] [--delete-placeholders] [--delete-duplicates]
"""

import json, os, urllib.request, urllib.error, sys, time

TOKEN = json.load(open(os.path.expandvars(r'%USERPROFILE%\keys.json')))['zenodo_token']
HEADERS = {'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/json'}
DELETE_HEADERS = {'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/json', 'Content-Type': 'application/json'}

DRY_RUN = '--dry-run' in sys.argv
DELETE_PLACEHOLDERS = '--delete-placeholders' in sys.argv
DELETE_DUPLICATES = '--delete-duplicates' in sys.argv

def get_all_pages(base_url, max_pages=50):
    """Paginate through Zenodo API results."""
    results = []
    url = base_url
    for page in range(max_pages):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req) as r:
                data = json.loads(r.read())
        except urllib.error.HTTPError as e:
            print(f'  HTTP {e.code} on page {page}')
            break
        hits = data.get('hits', {}).get('hits', [])
        if not hits:
            break
        results.extend(hits)
        links = data.get('links', {})
        if 'next' not in links:
            break
        url = links['next']
        time.sleep(0.3)
    return results

def search_by_subject(subject_term, label="records", size=200):
    """Search for records with a specific subject tag."""
    import urllib.parse
    encoded = urllib.parse.quote(subject_term)
    base = f'https://zenodo.org/api/records/?q=metadata.subjects.subject:"{encoded}"&size={size}&sort=mostrecent&state=done&all_versions=false'
    print(f'Searching for "{subject_term}" {label}...')
    return get_all_pages(base)

def delete_record(rec_id):
    """Delete a Zenodo record by ID."""
    url = f'https://zenodo.org/api/records/{rec_id}'
    req = urllib.request.Request(url, method='DELETE', headers=DELETE_HEADERS)
    try:
        with urllib.request.urlopen(req) as r:
            return True, f'HTTP {r.status}'
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        return False, f'HTTP {e.code}: {body[:200]}'

def main():
    print('=== ZENODO CLEANUP AUDIT ===')
    if DRY_RUN:
        print('DRY RUN MODE — no deletions will occur\n')

    # 1. Find PLACEHOLDER records
    placeholders = search_by_subject('PLACEHOLDER', 'PLACEHOLDER records')
    print(f'Found {len(placeholders)} PLACEHOLDER records')
    
    if placeholders:
        print('\n--- PLACEHOLDER records ---')
        for i, p in enumerate(placeholders[:20]):
            meta = p['metadata']
            title = meta.get('title', 'No title')
            print(f'  {p["id"]}: \"{(title[:60])}\"')
        if len(placeholders) > 20:
            print(f'  ... and {len(placeholders)-20} more')

        if DELETE_PLACEHOLDERS and not DRY_RUN:
            print(f'\nDeleting {len(placeholders)} PLACEHOLDER records...')
            deleted, failed = 0, 0
            for i, p in enumerate(placeholders):
                ok, msg = delete_record(p['id'])
                if ok:
                    deleted += 1
                    if deleted % 10 == 0:
                        print(f'  Deleted {deleted}/{len(placeholders)}...')
                else:
                    failed += 1
                    print(f'  FAILED {p["id"]}: {msg}')
                time.sleep(0.5)
            print(f'Result: {deleted} deleted, {failed} failed')
        elif DELETE_PLACEHOLDERS:
            print(f'  [DRY-RUN] Would delete {len(placeholders)} records')
    else:
        print('  No PLACEHOLDER records found.')

    # 2. Find duplicate records
    print()
    duplicates = search_by_subject('duplicate-record', 'duplicate records')
    print(f'Found {len(duplicates)} duplicate-record tagged entries')
    
    if duplicates:
        print('\n--- Duplicate records ---')
        for i, d in enumerate(duplicates[:20]):
            meta = d['metadata']
            title = meta.get('title', 'No title')[:80]
            creators = [c['name'] for c in meta.get('creators', [])]
            print(f'  {d["id"]}: \"{title}\" — by {creators}')
        if len(duplicates) > 20:
            print(f'  ... and {len(duplicates)-20} more')

        if DELETE_DUPLICATES and not DRY_RUN:
            print(f'\nDeleting {len(duplicates)} duplicate records...')
            deleted, failed = 0, 0
            for i, d in enumerate(duplicates):
                ok, msg = delete_record(d['id'])
                if ok:
                    deleted += 1
                else:
                    failed += 1
                    print(f'  FAILED {d["id"]}: {msg}')
                time.sleep(0.5)
            print(f'Result: {deleted} deleted, {failed} failed')
        elif DELETE_DUPLICATES:
            print(f'  [DRY-RUN] Would delete {len(duplicates)} records')
    else:
        print('  No duplicate records found.')

    print(f'\n--- SUMMARY ---')
    print(f'PLACEHOLDER: {len(placeholders)} records')
    print(f'Duplicate:   {len(duplicates)} records')
    print(f'Total to clean: {len(placeholders) + len(duplicates)}')

if __name__ == '__main__':
    main()
