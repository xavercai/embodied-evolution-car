"""Check mail-routing quality (MX / SPF / DMARC) for candidate email domains.

SPF and DMARC indicate how likely a foreign sender such as arxiv.org is to
have its message accepted rather than silently dropped.
"""

import subprocess
import ssl
import urllib.request

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

DOMAINS = [
    "gmail.com",
    "outlook.com",
    "hotmail.com",
    "yahoo.com",
    "icloud.com",
    "protonmail.com",
    "qq.com",
    "foxmail.com",
    "163.com",
    "126.com",
    "sina.com",
    "139.com",
    "189.cn",
    "aliyun.com",
    "volkswagen.com.cn",
]


def resolve(name, rtype):
    out = subprocess.run(
        ["nslookup", "-type=" + rtype, name],
        capture_output=True,
        text=True,
        timeout=60,
    )
    return out.stdout + out.stderr


def extract_blocks(text):
    """Split nslookup output into per-answer sections."""
    return text.split("Name:")


for d in DOMAINS:
    print(f"\n===== {d} =====")

    mx = resolve(d, "MX")
    mx_lines = [
        ln.strip()
        for ln in mx.splitlines()
        if "mail exchanger" in ln or "MX = " in ln
    ]
    print(f"  MX      : {mx_lines[:3] if mx_lines else 'none (CNAME/A-record fallback?)'}")

    if "can't find" in mx.lower() or "NONAME" in mx.upper() or not mx_lines:
        a = resolve(d, "A")
        a_lines = [
            ln.strip() for ln in a.splitlines() if "Address:" in ln or "Addresses:" in ln
        ]
        print(f"  A       : {a_lines[:3] if a_lines else 'none'}")

    spf = resolve(d, "TXT")
    has_spf = "v=spf1" in spf
    print(f"  SPF     : {'present' if has_spf else 'ABSENT'}")

    dmarc = resolve(f"_dmarc.{d}", "TXT")
    has_dmarc = "v=DMARC1" in dmarc
    print(f"  DMARC   : {'present' if has_dmarc else 'ABSENT'}")
