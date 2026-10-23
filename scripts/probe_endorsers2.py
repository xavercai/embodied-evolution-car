"""Locate the per-paper endorser link and the author contact entry points."""

import re
import ssl
import urllib.request

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

IDS = ["2603.12510", "2502.15937", "2410.02319", "2604.22551", "2508.19172"]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90, context=CTX) as resp:
        return resp.read().decode("utf-8", "ignore")


for aid in IDS:
    html = get(f"https://arxiv.org/abs/{aid}")

    m = re.search(
        r'<a href="([^"]+)"[^>]*>\s*Which authors of this paper are endorsers',
        html,
    )
    link = m.group(1) if m else None

    view_emails = re.findall(r'\[view email\]', html)
    mailto = re.findall(r'href="mailto:([^"]+)"', html)

    print(f"\n=== {aid} ===")
    print(f"endorser link : {link}")
    print(f"view email cnt: {len(view_emails)}   mailto: {mailto[:3]}")

    if link:
        url = link if link.startswith("http") else "https://arxiv.org" + link
        try:
            sub = get(url)
            names = re.findall(r"<a[^>]*>([^<]+)</a>", sub)
            keep = [
                n.strip()
                for n in names
                if n.strip()
                and "endorse" not in n.lower()
                and "arxiv" not in n.lower()
                and len(n.strip()) < 45
                and not n.strip().startswith(("Back", "Submit", "Please"))
            ]
            print(f"  -> endorser page names: {keep[:12]}")
        except Exception as exc:
            print(f"  -> fetch failed: {type(exc).__name__}")
