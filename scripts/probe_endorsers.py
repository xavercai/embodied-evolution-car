"""Check arXiv abs pages for endorser eligibility and visible contact emails."""

import re
import ssl
import urllib.request

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

IDS = [
    "2603.12510",  # Stefanos Nikolaidis - diversity / behavioral
    "2502.15937",  # Daniel S. Brown / Connor Mattson - novelty search
    "2410.02319",  # Stephane Doncieux - QD / novelty
    "2604.22551",  # Mahdi Khoramshahi - swarm / novelty
    "2508.19172",  # Antoine Cully - QD
    "2504.01915",  # Antoine Cully
    "2603.19582",  # Yue Xie
    "2403.19545",  # Jie Luo
]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90, context=CTX) as resp:
        return resp.read().decode("utf-8", "ignore")


for aid in IDS:
    try:
        html = get(f"https://arxiv.org/abs/{aid}")
    except Exception as exc:
        print(f"{aid}: FETCH FAILED {type(exc).__name__}")
        continue

    tm = re.search(r'<h1 class="title[^>]*>(.*?)</h1>', html, re.S)
    title = (
        " ".join(re.sub(r"<[^>]+>", "", tm.group(1)).split())
        if tm
        else "(title not parsed)"
    )

    has_endorser_link = "Which authors of this paper are endorsers?" in html
    endorser_block = re.findall(
        r"endorsers\?[^<]*</a>(.*?)</div>", html, re.S
    )
    endorser_names = []
    for blk in endorser_block:
        for nm in re.findall(r'<a href="/auth/endorse[^"]*"[^>]*>([^<]+)</a>', blk):
            endorser_names.append(nm.strip())

    emails = [
        e
        for e in re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html
        )
        if "arxiv.org" not in e
        and "creativecommons" not in e
        and "example" not in e.lower()
        and "domain" not in e.lower()
    ]
    emails = list(dict.fromkeys(emails))[:4]

    print(f"\n=== {aid} ===")
    print(f"title      : {title[:95]}")
    print(f"endorser UI: {has_endorser_link}")
    if endorser_names:
        print(f"endorsers  : {', '.join(endorser_names[:8])}")
    print(f"emails     : {emails if emails else '(none visible)'}")
