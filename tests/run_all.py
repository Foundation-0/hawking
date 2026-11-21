#!/usr/bin/env python3
"""Master R4-clean test runner for Foundation-0/hawking.

Executes:
  1. All four exact zero-float verification modules via `hawking.cli.run_verify("all")`
  2. Clean-room R5 test suite for `hawking.observer_sheaf_mdr`
  3. Clean-room R5 unittest suite for `hawking.boundary_double_schur_hodge`
  4. CLI smoke checks (`list`, `verify --module theorem --json`)

Zero third-party dependencies; zero bare `assert`s; bit-identical across all 4 isolated
R4 modes (`-I -B`, `-I -O -B`, `-I -B -W error`, `-I -O -B -W error`).
"""

from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = Path(__file__).resolve().parent
for p in (str(ROOT), str(TESTS_DIR)):
    if p not in sys.path:
        sys.path.insert(0, p)

from hawking import cli  # noqa: E402
import test_boundary_double_schur_r5  # noqa: E402
import test_observer_sheaf_mdr_r5  # noqa: E402


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError(f"HAWKING_TEST_RUNNER_FAILED: {msg}")


def main() -> int:
    # 1. All 4 exact zero-float verification modules
    bundle = cli.run_verify("all")
    require(bundle["all_verified"] is True, "Not all modules verified")
    require(bundle["modules_verified"] == 4, f"Expected 4 modules, got {bundle['modules_verified']}")
    require(bundle["zero_floats"] is True, "Float detected in verification output")

    # 2. Observer-Sheaf MDR R5 suite (AUDIT-043)
    mdr_groups = test_observer_sheaf_mdr_r5.run_all_tests()
    require(mdr_groups == 3, f"Expected 3 MDR test groups, got {mdr_groups}")

    # 3. Boundary Double-Schur / Surgical Krein-Severing / Ramanujan 2-Lift R5 unittest suite (AUDIT-047)
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_boundary_double_schur_r5)
    sink = io.StringIO()
    result = unittest.TextTestRunner(stream=sink, verbosity=0).run(suite)
    if not result.wasSuccessful():
        raise RuntimeError(f"Boundary Double-Schur R5 unittest failed:\n{sink.getvalue()}")

    # 4. CLI smoke checks (no disk side effects!)
    buf_list = io.StringIO()
    with redirect_stdout(buf_list):
        rc_list = cli.main(["list"])
    require(rc_list == 0 and "theorem" in buf_list.getvalue(), "CLI list check failed")

    buf_json = io.StringIO()
    with redirect_stdout(buf_json):
        rc_json = cli.main(["verify", "--module", "theorem", "--json"])
    require(rc_json == 0, "CLI verify --json failed")
    parsed = json.loads(buf_json.getvalue())
    require(parsed["all_verified"] is True and parsed["modules_verified"] == 1, "CLI JSON output invalid")

    print("=== Foundation-0/hawking FULL VERIFICATION PASS ===")
    for key, info in bundle["receipts"].items():
        print(f"  [PASS] {key:8s}  sha256={info['canonical_sha256']}")
    print(f"  [PASS] observer_sheaf_mdr R5 suite: {mdr_groups}/3 groups")
    print(f"  [PASS] boundary_double_schur_hodge R5 suite: {result.testsRun}/{result.testsRun} tests")
    print(f"  Bundle SHA-256: {bundle['bundle_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
