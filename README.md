# TACTIC-Review: Colab Feasibility Pilot

This repository contains the reproducible Google Colab workflow and evidence for a
small feasibility-oriented pilot of TACTIC-Review's target-aware executable admission mechanism.

## Scope

- Framework: ESP-IDF v5.5.4
- Sample: `examples/get-started/hello_world`
- Targets: ESP32 and ESP32-S3
- Environment: Google Colab, Linux x86_64
- Validation type: build-level controlled experiment
- Hardware required: none

## Main result

| Stage | ESP32 | ESP32-S3 | Admission |
|---|---:|---:|---:|
| Clean baseline | PASS | PASS | — |
| Controlled target-specific defect | FAIL | PASS | ADMIT |

The controlled claim was:

> The injected change breaks the ESP32 build while preserving the ESP32-S3 build.

The ESP32 build failed with the expected marker:

```text
TACTIC_TASK_01: controlled ESP32-only build failure
```

The ESP32-S3 build passed. Therefore, the executable admission rule returned `ADMIT`.

## Reproduce in Google Colab

1. Upload `notebooks/TACTIC_Review_Colab_Pilot.ipynb` to Google Colab.
2. Run cells from top to bottom.
3. The notebook installs ESP-IDF v5.5.4 and required tools in the temporary Colab runtime.
4. It builds clean baselines for both targets.
5. It injects the controlled target-specific defect.
6. It writes JSON evidence and build logs under `/content/tactic_pilot/results`.

A Colab runtime is temporary. Download the generated result files before closing the session.

## Repository structure

```text
TACTIC_Pilot_Colab_Repository/
├── notebooks/
│   └── TACTIC_Review_Colab_Pilot.ipynb
├── scripts/
│   ├── admission_gate.py
│   └── controlled_defect.c
├── results/
│   ├── baseline_summary.json
│   └── task_01_corrected_evidence.json
├── logs/
│   └── task_01_console_excerpt.txt
├── paper/
│   └── pilot_evaluation_text.md
├── LICENSE
├── CITATION.cff
└── README.md
```

## Interpretation boundary

This is a preliminary feasibility pilot, not a comprehensive benchmark. It validates one
controlled build-level target divergence in one ESP-IDF sample project. It does not evaluate
LLM-generated candidate quality, multiple repositories, hardware execution, or developer trust.

## Citation

See `CITATION.cff`.
