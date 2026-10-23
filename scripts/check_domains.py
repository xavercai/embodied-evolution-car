"""Classify candidate email domains using the Leiden scholarly-domain dataset.

Dataset: "Classification of domain names of scholarly email addresses"
(Luwel & van Eck, 2023) - labels domains as institutional or non-institutional.
Also probes MX records to check whether the domain can receive mail at all.
"""

import re
import ssl
import urllib.request

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

DOMAINS = [
    "gmail.com",
    "outlook.com",
    "hotmail.com",
    "live.com",
    "yahoo.com",
    "icloud.com",
    "protonmail.com",
    "qq.com",
    "foxmail.com",
    "163.com",
    "126.com",
    "sina.com",
    "sohu.com",
    "139.com",
    "189.cn",
    "aliyun.com",
    "volkswagen.com.cn",
]

DS = "https://zenodo.org/records/7851620/files/email_domain_name_classification.txt"


def get(url, timeout=180):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read()
    except Exception as exc:
        return -1, f"{type(exc).__name__}: {exc}".encode()


st, raw = get(DS)
print(f"dataset fetch: status={st} size={len(raw)}")

classification = {}
if st == 200:
    text = raw.decode("utf-8", "ignore")
    for line in text.splitlines():
        parts = re.split(r"\s+", line.strip())
        if len(parts) >= 2:
            classification[parts[0].lower()] = parts[1]
    print(f"parsed {len(classification)} domains\n")

print(f"{'domain':<26}{'scholarly class':<18}")
print("-" * 44)
for d in DOMAINS:
    cls = classification.get(d, "(not in dataset)")
    print(f"{d:<26}{cls:<18}")

print("\n=== MX record check (can the domain receive mail?) ===")
for d in DOMAINS:
    code, body = get(f"https://dns.google/resolve?name={d}&type=MX", timeout=60)
    txt = body.decode("utf-8", "ignore") if isinstance(body, bytes) else ""
    mxs = re.findall(r'"data":"([^"]+)"', txt)
    mx = mxs[0][:46] if mxs else "NO MX RECORD"
    print(f"{d:<26}{mx}")
