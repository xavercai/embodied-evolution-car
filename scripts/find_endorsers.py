"""Find arXiv authors eligible to endorse in the cs endorsement domain.

Eligibility rules (arxiv.org/help/endorsement):
  - endorser must have authored enough papers in the endorsement domain (cs)
  - only papers submitted between 3 months and 5 years ago are counted
  - the author must be registered as an author of the paper

For each candidate we report the arXiv id, the submission date, and the
author list, so the user can open the abs page and read the email address
under "Submission history".
"""

import datetime as dt
import re
import ssl
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "http://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}

QUERIES = [
    'cat:cs.RO AND abs:"novelty search"',
    'cat:cs.AI AND abs:"novelty search"',
    'cat:cs.RO AND abs:"quality diversity"',
    'cat:cs.RO AND abs:"evolutionary robotics"',
    'cat:cs.LG AND abs:"behavioral diversity" AND cat:cs.RO',
    'cat:cs.RO AND abs:"embodied intelligence" AND abs:"evolution"',
]

NOW = dt.datetime.now(dt.timezone.utc)


def fetch(query, max_results=40):
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": max_results,
        }
    )
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(
        f"{API}?{params}", headers={"User-Agent": "endorser-finder/1.0"}
    )
    with urllib.request.urlopen(req, timeout=90, context=ctx) as resp:
        return resp.read()


def parse(raw):
    root = ET.fromstring(raw)
    out = []
    for entry in root.findall("a:entry", NS):
        raw_id = entry.findtext("a:id", "", NS)
        arxiv_id = raw_id.rsplit("/abs/", 1)[-1]
        title = " ".join(entry.findtext("a:title", "", NS).split())
        published = entry.findtext("a:published", "", NS)
        authors = [
            a.findtext("a:name", "", NS) for a in entry.findall("a:author", NS)
        ]
        cats = [
            c.get("term") for c in entry.findall("a:category", NS)
        ]
        out.append(
            {
                "id": arxiv_id,
                "title": title,
                "published": published,
                "authors": authors,
                "cats": cats,
            }
        )
    return out


def main():
    papers = {}
    for q in QUERIES:
        try:
            for p in parse(fetch(q)):
                papers.setdefault(p["id"], p)
        except Exception as exc:  # network hiccup on one query shouldn't kill the run
            print(f"query failed: {q} -> {type(exc).__name__}: {exc}")

    eligible = []
    for p in papers.values():
        pub = dt.datetime.strptime(p["published"], "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=dt.timezone.utc
        )
        age_days = (NOW - pub).days
        if not (90 < age_days < 1825):
            continue
        eligible.append((age_days, p))

    eligible.sort(key=lambda t: t[0])

    seen_author = {}
    for age_days, p in eligible:
        for name in p["authors"]:
            seen_author.setdefault(name, []).append((age_days, p["id"], p["title"]))

    print(f"papers scanned: {len(papers)}  eligible-window papers: {len(eligible)}")
    print(f"distinct authors: {len(seen_author)}\n")

    ranked = sorted(
        seen_author.items(), key=lambda kv: len(kv[1]), reverse=True
    )
    print("=== authors ranked by number of eligible cs-domain papers ===")
    for name, items in ranked:
        ids = ", ".join(i[1] for i in items[:6])
        print(f"{len(items):2d}  {name}\n      {ids}")

    print("\n=== paper list ===")
    for age_days, p in eligible:
        cats = ",".join(p["cats"][:3])
        print(
            f"{p['id']:<16} {p['published'][:10]}  [{cats}]  "
            f"{p['title'][:70]}\n      authors: {', '.join(p['authors'])}"
        )


if __name__ == "__main__":
    main()
