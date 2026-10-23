# -*- coding: utf-8 -*-
"""生成英文标签的论文图表（用于 LaTeX / arXiv）。"""
import os, glob, re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(REPO, "data", "oee_data10192", "oee_data")
OUT  = os.path.join(REPO, "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False
# arXiv 的 PDF 处理管线不保留 Type 3 字体，必须嵌入 TrueType
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

oe = pd.read_csv(os.path.join(ROOT, "spiffs_raw", "oe_history.csv"), comment="#")
oe = oe[oe.generation <= 10]
D = pd.concat([pd.read_csv(f, comment="#").assign(
    gen=int(re.match(r'nova_gen_(\d+)', os.path.basename(f)).group(1)))
    for f in sorted(glob.glob(os.path.join(ROOT, "csv_converted", "nova_gen", "nova_gen_*.csv")))],
    ignore_index=True)

def noise_series():
    snap = os.path.join(ROOT, "csv_converted", "chaos_snapshots")
    arr = []
    for f in glob.glob(os.path.join(snap, "chaos_snaps_*.csv")):
        df = pd.read_csv(f)
        for c in ("rawNoiseL", "rawNoiseR"):
            if c in df.columns:
                arr.append(df[c].values)
    return np.concatenate(arr)

def mad_clean_med(oe):
    med = oe["noveltyScore"].median(); mad = np.median(np.abs(oe["noveltyScore"] - med))
    keep = (oe["noveltyScore"] - med).abs() <= 3.5 * mad
    return oe[keep].groupby("generation")["noveltyScore"].median()

nov_med = mad_clean_med(oe)
rc_mean = oe.groupby("generation")["ruleCount"].mean()

# ---- Fig: novelty + rules ----
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.4))
ax = axes[0]
ax.plot(nov_med.index, nov_med.values, "o-", color="#1f77b4", lw=1.6, ms=5)
ax.axhline(nov_med.iloc[-5:].mean(), ls="--", color="gray", lw=1)
ax.set_title("(a) Novelty: rise-then-plateau")
ax.set_xlabel("Generation"); ax.set_ylabel("Median novelty (MAD-clean)")
ax.grid(alpha=.3)
ax = axes[1]
ax.plot(rc_mean.index, rc_mean.values, "s-", color="#2ca02c", lw=1.6, ms=5)
ax.axhline(2, ls="--", color="gray", lw=1)
sl = stats.linregress(rc_mean.index.values.astype(float), rc_mean.values).slope
ax.set_title("(b) Rule count non-degeneration (slope %+.2f)" % sl)
ax.set_xlabel("Generation"); ax.set_ylabel("Mean rule count")
ax.grid(alpha=.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig_novelty_rules.pdf"), dpi=150)
fig.savefig(os.path.join(OUT, "fig_novelty_rules.png"), dpi=150); plt.close(fig)

# ---- Fig: GPIO6 noise ----
noise = noise_series()
fig, ax = plt.subplots(figsize=(7.2, 3.1))
ax.hist(noise, bins=40, range=(0, 4095), color="#d62728", alpha=.7, edgecolor="k", lw=.3)
ax.axvline(noise.mean(), color="k", ls="--", lw=1.2, label="mean %.0f" % noise.mean())
ax.axvspan(0, 423, color="orange", alpha=.15, label="occupied range 0-423")
ax.set_title("GPIO6 post-hoc hardware audit: rawNoise distribution (12-bit full scale 0-4095)")
ax.set_xlabel("rawNoise ADC reading"); ax.set_ylabel("Frame count")
ax.legend(fontsize=8); ax.grid(alpha=.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig_noise_hist.pdf"), dpi=150)
fig.savefig(os.path.join(OUT, "fig_noise_hist.png"), dpi=150); plt.close(fig)

# ---- Fig: anchoring ----
d = D[D.chaosFrameRatio > 0]
pl = (d.chaosSpeedDeltaL < 0).mean()
bio = D.groupby("gen")[["forwardRatio", "turnRatio", "reverseRatio", "idleRatio"]].mean()
r_tr = stats.spearmanr(bio["turnRatio"], bio["reverseRatio"]).statistic

fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.4))
ax = axes[0]
ax.hist(d.chaosSpeedDeltaL, bins=22, color="#1f77b4", alpha=.6, edgecolor="k", lw=.3)
ax.axvline(0, color="k", lw=1)
ax.set_title("(a) Chaos constrained to left-wheel deceleration  P(dL<0)=%.2f" % pl)
ax.set_xlabel("Left wheel speed delta dL"); ax.set_ylabel("Count")
ax.grid(alpha=.3)
ax = axes[1]
ax.plot(bio.index, bio["turnRatio"], "o-", color="#ff7f0e", label="Turn")
ax.plot(bio.index, bio["reverseRatio"], "s-", color="#2ca02c", label="Reverse")
ax.plot(bio.index, bio["forwardRatio"], "^-", color="#1f77b4", label="Forward")
ax.set_title("(b) Turn/reverse complementary axis  (r=%.2f)" % r_tr)
ax.set_xlabel("Generation"); ax.set_ylabel("Behavior proportion")
ax.legend(fontsize=8); ax.grid(alpha=.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig_anchoring.pdf"), dpi=150)
fig.savefig(os.path.join(OUT, "fig_anchoring.png"), dpi=150); plt.close(fig)

print("novelty gen1=%.3f plateau=%.3f" % (nov_med.iloc[0], nov_med.iloc[-5:].mean()))
print("rule gen10=%.2f all=%.2f" % (rc_mean[10], rc_mean.mean()))
print("noise min=%d max=%d mean=%.1f std=%.1f" % (noise.min(), noise.max(), noise.mean(), noise.std()))
print("P(dL<0)=%.3f r(turn,reverse)=%.2f" % (pl, r_tr))
print("chfr mean=%.3f" % D.groupby("gen")["chaosFrameRatio"].mean().mean())
print("DONE figures ->", OUT)