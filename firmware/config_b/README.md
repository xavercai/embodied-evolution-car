# Config B — N16R8 (FFat)

Extended-board firmware: ESP32-S3-N16R8 (16 MB Flash + 8 MB PSRAM), TCRT5000 reflective sensor, FFat filesystem.

## Files

| Path | Description |
|---|---|
| `OEETestFinal_v10_12_EXSIMP_N16R8_FFat.ino` | Frozen N16R8/FFat build (v10.12-EXSIMP). 2026-10-13: N16R8 swap + FFat migration, min retained generations 10 / max 100, L/R encoder ENCB pins completed. |
| `partitions_16m.csv` | FFat partition table for the 16 MB module (app0 3 MB + FFat 12 MB). |

## How it differs from Config A

| Item | Config A | Config B (this dir) |
|---|---|---|
| Board | ESP32-S3-M-4M | ESP32-S3-N16R8 |
| Filesystem | SPIFFS | FFat |
| Sensor | Sharp GP2Y0A21YK0F | TCRT5000 (AO analog out) |
| IR pins | GPIO4 / GPIO5 | GPIO1 / GPIO2 |
| Motor driver | DRV8833 | L298N |

The two builds share the same EXSIMP persistence core and behavior-rule engine; this `.ino` is the N16R8/FFat variant with the Config-B pin map and FFat mount logic. For the shared firmware invariants (packed structs, two-stage atomic writes, DATA-PRESERVED) see [`../README.md`](../README.md).