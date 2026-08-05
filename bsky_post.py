#!/usr/bin/env python3
"""Bluesky posting — AT Protocol minimal client, zero dependencies."""
import urllib.request, urllib.error, json, os, sys, time

BSKY_API = "https://bsky.social/xrpc"

def _req(method, endpoint, body=None, headers=None):
    url = f"{BSKY_API}/{endpoint}"
    data = json.dumps(body).encode() if body else None
    hdrs = {"Content-Type": "application/json"}
    if headers: hdrs.update(headers)
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        err = json.loads(e.read())
        raise RuntimeError(f"AT Protocol error: {err.get('message', str(err))}")

def create_session(handle, app_pass):
    return _req("POST", "com.atproto.server.createSession",
                {"identifier": handle, "password": app_pass})

def post_text(session, text, reply_to=None, facets=None):
    """Post text to Bluesky.
    
    Args:
        session: Auth session dict (must have 'did' and 'accessJwt')
        text: Post text (max 300 graphemes)
        reply_to: Optional dict with 'root' and 'parent' AT-URI refs
        facets: Optional list of rich-text facet objects
    """
    record = {
        "$type": "app.bsky.feed.post",
        "text": text,
        "createdAt": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
    }
    if facets:
        record["facets"] = facets
    if reply_to:
        record["reply"] = reply_to
    
    headers = {"Authorization": f"Bearer {session['accessJwt']}"}
    result = _req("POST", "com.atproto.repo.createRecord",
                  {"repo": session["did"],
                   "collection": "app.bsky.feed.post",
                   "record": record},
                  headers=headers)
    return result

def make_link_facet(text, url):
    """Create a facet object for a link in text."""
    start = 0
    # For simplicity, find the URL or its label in the text
    pass

def main():
    handle = os.environ.get("BSKY_HANDLE")
    app_pass = os.environ.get("BSKY_APP_PASS")
    
    if not handle or not app_pass:
        print("ERROR: Set BSKY_HANDLE and BSKY_APP_PASS environment variables")
        sys.exit(1)
    
    # Read posts from stdin or args
    if len(sys.argv) < 2:
        text = sys.stdin.read().strip()
    else:
        subcmd = sys.argv[1]
        if subcmd == "post":
            text = sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read().strip()
        elif subcmd == "thread":
            # Read thread posts: one per line, separated by ---THREAD--- markers
            posts = sys.argv[2:] if len(sys.argv) > 2 else []
            if not posts:
                raw = sys.stdin.read().strip()
                posts = [p.strip() for p in raw.split("---THREAD---") if p.strip()]
        else:
            text = subcmd
    
    session = create_session(handle, app_pass)
    print(f"Authenticated as: {session['handle']} (DID: {session['did']})")
    
    if subcmd == "thread" and 'posts' in dir():
        parent_uri = None
        root_uri = None
        for i, post_text in enumerate(posts):
            reply_to = None
            if i > 0:
                reply_to = {"root": {"uri": root_uri, "cid": root_cid},
                          "parent": {"uri": parent_uri, "cid": parent_cid}}
            
            result = post_text(session, post_text, reply_to=reply_to)
            uri = result["uri"]
            cid = result["cid"]
            print(f"Post {i+1}/{len(posts)}: {post_text[:60]}... → {uri}")
            
            if i == 0:
                root_uri, root_cid = uri, cid
            parent_uri, parent_cid = uri, cid
            
            time.sleep(1.5)  # Rate limit
    else:
        result = post_text(session, text)
        print(f"Posted: {result['uri']}")

if __name__ == "__main__":
    main()
