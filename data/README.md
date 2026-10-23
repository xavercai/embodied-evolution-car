# Data

Experimental datasets for the paper. Raw binary exports are large; keep them under Git LFS or an external store if the repository grows beyond GitHub's size limits.

## Dataset layout (per run)

```
oee_data_<id>/
└── oee_data/                    # root inside the source zip
    ├── data_summary.txt         # v5.8 pipeline report: SPIFFS/RAM download + BIN conversion checks
    ├── spiffs_raw/
    │   ├── oe_history.csv       # per-individual metadata: novelty, survival, rule count
    │   ├── chaos_history.csv    # chaos-snapshot history (may be binary-polluted in some batches)
    │   ├── individual_csv/      # per-individual behavior-rule tables (gen_<g>_id_<i>.csv)
    │   ├── frame_bin/           # raw 11-byte compressed frame logs
    │   ├── chaos_snap_bin/      # raw per-frame chaos snapshot binaries
    │   ├── nova_gen_bin/        # per-generation descriptor binaries
    │   ├── pop_bin/             # population-state binaries
    │   └── chaos_record_csv/    # per-record chaos CSV
    ├── csv_converted/
    │   ├── nova_gen/            # per-generation behavioral descriptors
    │   ├── frame_logs/          # decompressed 11-byte frame logs
    │   ├── chaos_snapshots/     # per-frame chaos snapshots (rawNoiseL/R, sensor, PWM)
    │   ├── populations/         # per-generation population tables (+ *_rules.csv)
    │   └── validation_report.json
    └── ram_data/                # RAM snapshot at download time (schema/status/file_list + snapshot CSVs)
```

## Known acquisition defects

Two defects in the extended (Config B) batch must be accounted for in any downstream analysis:

- `distance_ticks` is uniformly `0` — encoder odometry produced no counts on the N16R8 bring-up.
- `survival_time` is capped at ~25 s (25001–26238 ms) — the test-duration cap removed variance.

These make speed, survival-variance, and the A/B/C/D four-class differencing **non-recomputable** for that batch. They are acquisition gaps, not negated conclusions.

## Reproducing the figures

```bash
python scripts/generate_figs_en.py
```

The script reads `oe_history.csv`, `nova_gen/*.csv`, and `chaos_snapshots/*.csv` and outputs the three paper figures into `figures/`.

## Terms

Data are released for research use. If you use them in a publication, please cite the paper (see the top-level README).