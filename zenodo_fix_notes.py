import urllib.request, urllib.error, json

# Since we can't easily use the browser to edit the form,
# let's document the fix approach:
print("""
=== ZENODO ATTRIBUTION FIX — RECORD 21789920 ===

RECORD: "Five Pillars, One Structure: Consilient Convergence in QNFO Research [KIF-60 Assessed 2026-08-04]"
DOI: 10.5281/zenodo.21789920
CURRENT AUTHOR: "QNFO Research Collective"  <-- VIOLATES ADR-014
TARGET AUTHOR: "Rowan Brad Quni-Gudzinas"     <-- ADR-014 compliant

FIX INSTRUCTIONS:
1. Go to: https://zenodo.org/uploads/21789920
2. In the "Authors/Creators" section, click the "Edit" button next to "QNFO Research Collective"
3. Change to: Rowan Brad Quni-Gudzinas (given name: Rowan Brad, family name: Quni-Gudzinas)
4. Add ORCID: 0009-0002-4317-5604
5. Click "Save" then "Publish"

This is the single highest-leverage fix for AI search:
any AI system that pulls from Zenodo metadata will see this as the
canonical author instead of an anonymous collective.
""")
