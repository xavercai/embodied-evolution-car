# Config B — N16R8 (reserved)

This directory is reserved for the extended-board firmware (ESP32-S3-N16R8, TCRT5000, FFat).

## Current status

Config B **currently shares the single EXSIMP source** in `../config_a/OEETestFinal_v10_12_EXSIMP.ino`. There is no separate Config B build yet — the two boards differ only at flash time:

| Item | Config A (baseline) | Config B (extended) |
|---|---|---|
| Board | ESP32-S3-M-4M (N4R2) | ESP32-S3-N16R8 |
| Sensor | Sharp | TCRT5000 |
| Sensor pins | GPIO4 / GPIO5 | GPIO1 / GPIO2 |
| Filesystem | SPIFFS | FFat |

## When to place a dedicated source here

Add a Config B-specific `.ino` (or split the shared core into `../shared/`) only if the two configurations diverge in source — for example a distinct sensor driver, an FFat-specific persistence path, or an N16R8-only memory layout (16 MB Flash + 8 MB PSRAM). Until then, keep the frozen EXSIMP source in `config_a/` as the single source of truth.