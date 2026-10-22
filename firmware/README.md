# Firmware

This directory holds the ESP32 firmware for both hardware configurations. The source is maintained separately and imported here for release.

## Files to place here

| Path | Description |
|---|---|
| `config_a/` | Baseline (ESP32-S3-M-4M, Sharp sensor, SPIFFS/EXSIMP) firmware |
| `config_b/` | Extended (ESP32-S3-N16R8, TCRT5000, FFat) firmware |
| `shared/`  | Novelty-search core, behavior-rule engine, chaos intervention |

## Firmware invariants (required by the analysis)

The paper's conclusions depend on the following low-level contracts. Any firmware imported here **must** preserve them:

1. **"Three-no" principle** — no sensor calibration, no signal filtering, no PID control. The raw hardware thermal noise on the floating pin is a *system input*, not a disturbance to remove.
2. **Structure-first data pipeline**
   - All persisted structs declared `__attribute__((packed))`.
   - Variable-length serialization + fixed-width delta compression (frame log = 11 bytes).
   - Every binary file begins with a 4-byte magic number + version + CRC32.
   - Two-stage atomic writes: `temp file → verify → rename`.
3. **EXSIMP persistence** (protocol freeze, 2023-09-16) — the terminal data-pipeline convention.
4. **DATA PRESERVED** — anti-accidental-deletion policy across filesystem migrations (SPIFFS → FFat).

## Protocol freeze note

Data epochs are separated by firmware-version provenance. Pre-freeze (pre-EXSIMP) data are kept traceable via pin assignment (GPIO4/5 vs GPIO1/2) and file-header metadata. Do **not** regenerate old datasets from mixed-version source.

## Dependencies

The frozen **EXSIMP** build has **zero third-party dependencies**. It compiles on the Arduino ESP32 core plus the C++ standard library only.

### Build requires

| Requirement | Version | Notes |
|---|---|---|
| Arduino ESP32 core | `>= 2.0.6` | The `File.name()` behavior changed at 2.0.6; the code assumes the fixed behavior. |
| Board | ESP32-S3 (N16R8 / N8R8) | Config B = N16R8 (16 MB Flash + 8 MB PSRAM); Config A = N4R2. |
| Partition scheme | SPIFFS (Config A) / FFat (Config B) | Config B requires a FFat partition table. |

### Headers actually used by the frozen build

```cpp
// C++ standard library
#include <algorithm> <cmath> <cstdarg> <cstdio> <cstring> <vector>
// ESP32 core
#include <esp_random.h>   // on-chip TRNG (physical true-random source)
#include <FS.h>           // filesystem abstraction
#include <SPIFFS.h>       // SPIFFS (Config A)
#include <WiFi.h>         // Wi-Fi (used by the web/log endpoint)
#include <WebServer.h>    // synchronous web server (log export)
```

### Physical randomness sources

Two independent physical sources feed the chaos mechanism:

1. `esp_random()` — the ESP32-S3 on-chip TRNG;
2. a floating ADC pin (GPIO6) read as an analog noise source.

> Note on GPIO6: on the N16R8 module GPIO6 is multiplexed with internal Flash, so the second source degrades to low-amplitude coupling noise (see the paper, Section 4.2 / post-hoc hardware audit). Functional behavior is preserved (`esp_random` remains), but noise *quality* is reduced.

### Legacy (pre-EXSIMP) libraries — NOT required

Earlier versions used third-party libraries that the frozen build has since removed:

- ArduinoJson
- AsyncTCP / ESP_Async_WebServer / ESPAsyncTCP
- PubSubClient (MQTT)

These live under `Arduino/libraries/` in the working tree for historical revisions only; do **not** add them back into the frozen build.