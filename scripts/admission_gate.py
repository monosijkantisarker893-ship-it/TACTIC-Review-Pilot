#!/usr/bin/env python3
"""Minimal admission gate used by the TACTIC-Review feasibility pilot."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def decide(evidence: dict) -> str:
    esp32 = evidence["changed_results"]["esp32"]
    esp32s3 = evidence["changed_results"]["esp32s3"]

    supported = (
        evidence["baseline"]["esp32"] == "PASS"
        and evidence["baseline"]["esp32s3"] == "PASS"
        and esp32["status"] == "FAIL"
        and esp32["failure_marker_found"] is True
        and esp32s3["status"] == "PASS"
    )
    return "ADMIT" if supported else "ABSTAIN"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_json", type=Path)
    args = parser.parse_args()

    evidence = json.loads(args.evidence_json.read_text(encoding="utf-8"))
    decision = decide(evidence)
    print(decision)


if __name__ == "__main__":
    main()
