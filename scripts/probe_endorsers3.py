"""Probe show-endorsers endpoint and locate arXiv institutional-email domain logic."""

import json
import re
import ssl
import urllib.request

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def get(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
            return resp.status, resp.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "ignore")[:300]
    except Exception as exc:
        return -1, f"{type(exc).__name__}: {exc}"


print("=== show-endorsers endpoint ===")
for aid in ["2603.12510", "2410.02319"]:
    st, body = get(f"https://arxiv.org/auth/show-endorsers/{aid}")
    names = re.findall(r'<a[^>]*>([A-Z][A-Za-z.\- ]{2,40})</a>', body)
    print(f"{aid}: status={st} names={names[:10]}")
    if st == 200:
        print("   snippet:", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))[:300])

print("\n=== arXiv source: paths mentioning email/domain ===")
st, body = get(
    "https://api.github.com/repos/arXiv/arxiv/git/trees/master?recursive=1"
)
if st == 200:
    tree = json.loads(body).get("tree", [])
    hits = [
        t["path"]
        for t in tree
        if "email" in t["path"].lower() or "domain" in t["path"].lower()
    ]
    print(f"total paths: {len(tree)}  matches: {len(hits)}")
    for p in hits[:40]:
        print("  ", p)
else:
    print("tree fetch failed", st, body[:200])
