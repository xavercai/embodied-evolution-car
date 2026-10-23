# -*- coding: utf-8 -*-
"""打包 arXiv 提交件。

arXiv 的自动编译管线要求：
  - 主 .tex 位于提交根目录
  - 所有文件路径为相对路径（``../figures/`` 之类的绝对/上跳路径会编译失败）
  - 图件放在子目录时用 \\graphicspath 声明
本脚本从仓库源码生成一个可直接上传的 .tar.gz。
"""
import os
import re
import shutil
import tarfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_TEX = os.path.join(REPO, "paper", "main.tex")
FIG_DIR = os.path.join(REPO, "figures")
BUILD = os.path.join(REPO, "build", "arxiv")
STAGE = os.path.join(BUILD, "arxiv_submission")
ARCHIVE = os.path.join(BUILD, "arxiv_submission.tar.gz")

FIGURES = ["fig_noise_hist.pdf", "fig_novelty_rules.pdf", "fig_anchoring.pdf"]


def main():
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(os.path.join(STAGE, "figures"))

    tex = open(SRC_TEX, encoding="utf-8").read()

    # 仓库内 main.tex 用 ../figures/ 定位图件；arXiv 端改为子目录 figures/
    # 需匹配完整的花括号对：\graphicspath{{../figures/}{figures/}{}}
    tex = re.sub(r"\\graphicspath\{(?:[^{}]|\{[^{}]*\})*\}", lambda m: r"\graphicspath{{figures/}{}}", tex)

    # 去掉 TeX 注释：arXiv 会连同源码一起归档
    tex = re.sub(r"(?m)^\s*%.*$", "", tex)

    open(os.path.join(STAGE, "main.tex"), "w", encoding="utf-8").write(tex)

    for name in FIGURES:
        shutil.copy2(os.path.join(FIG_DIR, name), os.path.join(STAGE, "figures", name))

    if os.path.exists(ARCHIVE):
        os.remove(ARCHIVE)
    with tarfile.open(ARCHIVE, "w:gz") as tar:
        for name in sorted(os.listdir(STAGE)):
            tar.add(os.path.join(STAGE, name), arcname=name)

    _validate()

    total = sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, _, fs in os.walk(STAGE)
        for f in fs
    )
    print("staged  :", STAGE)
    for dp, _, fs in os.walk(STAGE):
        for f in sorted(fs):
            p = os.path.join(dp, f)
            print(f"   {os.path.relpath(p, STAGE):28s} {os.path.getsize(p)/1024:8.1f} KB")
    print("archive :", ARCHIVE, f"({os.path.getsize(ARCHIVE)/1024:.1f} KB, staged {total/1024:.1f} KB)")
    print("DONE arxiv package ->", ARCHIVE)


def _validate():
    """构建后自检：镜像 arXiv 自动编译管线的失败条件。"""
    tex = open(os.path.join(STAGE, "main.tex"), encoding="utf-8").read()
    problems = []

    if not os.path.isfile(os.path.join(STAGE, "main.tex")):
        problems.append("main.tex is not at the archive root")

    for m in re.findall(r"\\(?:includegraphics|input|bibliography)\{([^}]*)\}", tex):
        if m.startswith("/") or ".." in m or re.match(r"^[A-Za-z]:", m):
            problems.append(f"non-relative path: {m}")

    if re.search(r"\\include\{", tex):
        problems.append("\\include used; arXiv requires \\input")

    gp = re.search(r"\\graphicspath\{((?:[^{}]|\{[^{}]*\})*)\}", tex)
    if not gp:
        problems.append("no \\graphicspath declared")
    paths = [p.strip() for p in re.findall(r"\{([^{}]*)\}", gp.group(1))] if gp else []
    for g in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", tex):
        cands = [os.path.join(STAGE, p, g) for p in paths] + [os.path.join(STAGE, g)]
        if not any(os.path.isfile(c) for c in cands):
            problems.append(f"figure not resolvable from archive root: {g}")

    labels = set(re.findall(r"\\label\{([^}]*)\}", tex))
    refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]*)\}", tex))
    if refs - labels:
        problems.append(f"dangling \\ref: {sorted(refs - labels)}")

    cited = set()
    for c in re.findall(r"\\cite[a-zA-Z]*\{([^}]*)\}", tex):
        cited |= {k.strip() for k in c.split(",")}
    bibs = set(re.findall(r"\\bibitem\{([^}]*)\}", tex))
    if cited - bibs:
        problems.append(f"cited but no \\bibitem: {sorted(cited - bibs)}")

    if re.search(r"(?m)^\s*%", tex):
        problems.append("TeX comments remain in source")

    for f in sorted(os.listdir(os.path.join(STAGE, "figures"))):
        blob = open(os.path.join(STAGE, "figures", f), "rb").read()
        if re.search(rb"/Subtype\s*/Type3", blob):
            problems.append(f"Type 3 font in {f} (arXiv rejects bitmap fonts)")

    if problems:
        raise SystemExit("arXiv package validation failed:\n  - " + "\n  - ".join(problems))
    print("validation: passed")


if __name__ == "__main__":
    main()
