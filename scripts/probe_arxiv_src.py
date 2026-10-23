"""Locate arXiv source code that decides which email domains count as institutional."""

import json
import ssl
import urllib.request

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def get(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
            return resp.status, resp.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "ignore")[:200]
    except Exception as exc:
        return -1, f"{type(exc).__name__}: {exc}"


for repo, ref in [
    ("arXiv/arxiv", "master"),
    ("arXiv/arxiv", "main"),
    ("arXiv/arxiv-next", "master"),
]:
    st, body = get(
        f"https://api.github.com/repos/{repo}/git/trees/{ref}?recursive=1"
    )
    if st != 200:
        print(f"{repo}@{ref}: {st}")
        continue
    tree = json.loads(body).get("tree", [])
    hits = [
        t["path"]
        for t in tree
        if t.get("type") == "blob"
        and (
            "email" in t["path"].lower()
            or "domain" in t["path"].lower()
            or "institution" in t["path"].lower()
        )
    ]
    print(f"\n=== {repo}@{ref}: {len(tree)} paths, {len(hits)} matches ===")
    for p in hits[:50]:
        print("  ", p)
