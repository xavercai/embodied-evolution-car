"""Inspect the live arXiv registration form for domain-validation logic."""

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
        return exc.code, exc.read().decode("utf-8", "ignore")
    except Exception as exc:
        return -1, f"{type(exc).__name__}: {exc}"


st, html = get("https://arxiv.org/user/register")
print(f"register page status={st} len={len(html)}")

if st == 200:
    for kw in [
        "institutional",
        "Institutional",
        "domain",
        "organization",
        "Independent",
        "affiliation",
    ]:
        hits = [m.start() for m in re.finditer(kw, html)]
        print(f"  '{kw}': {len(hits)} hits")

    # print the field-legend block around organization/email
    for kw in ["Organization", "organization", "Independent"]:
        i = html.find(kw)
        if i > 0:
            seg = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html[max(0, i - 400):i + 700]))
            print(f"\n--- context around '{kw}' ---\n{seg[:900]}")
            break

    scripts = re.findall(r'src="([^"]+\.js[^"]*)"', html)
    print("\njs assets:", scripts[:12])

print("\n=== try known arXiv endpoints ===")
for path in [
    "/help/faq/email",
    "/help/faq/main",
    "/auth/institutional-email",
    "/user/register_email",
]:
    s, b = get("https://arxiv.org" + path)
    print(f"{path}: status={s} len={len(b)}")
