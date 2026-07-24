# Text for the six-page paper

## Experimental setup

We conducted a feasibility-oriented pilot evaluation using ESP-IDF v5.5.4 and
the official `examples/get-started/hello_world` sample. The experiment executed
in a Linux x86_64 Google Colab runtime and required no physical hardware.
Independent project workspaces were configured for ESP32 and ESP32-S3. We first
verified that the unmodified sample compiled successfully for both targets.
We then injected a controlled compile-time defect guarded by the ESP32 target
configuration macro and rebuilt both workspaces.

## Results

| Stage | ESP32 | ESP32-S3 | Admission |
|---|---:|---:|---:|
| Clean baseline | PASS | PASS | — |
| Controlled defect | FAIL | PASS | ADMIT |

The clean baseline compiled successfully for both ESP32 and ESP32-S3. After the
controlled target-specific change, the ESP32 build failed with the expected
diagnostic marker, whereas the ESP32-S3 build remained successful. Because the
observed target divergence matched the claim's executable obligation, the
admission gate returned `ADMIT`. This result provides preliminary evidence that
TACTIC-Review can gate a target-specific review claim using reproducible build
evidence.

## Limitations

This evaluation is intentionally limited to one ESP-IDF sample, two targets,
one controlled defect, and a build-level oracle. It is a feasibility pilot, not
a comprehensive benchmark. The study does not evaluate model-generated
candidate quality, additional repositories or defect families, hardware
execution, or developer trust.
