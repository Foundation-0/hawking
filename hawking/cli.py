"""Unified zero-dependency CLI for Foundation-0/hawking.

Usage:
    python3 -m hawking verify [--json] [--module all|horizon|padic|mdr|theorem]
    python3 -m hawking list
"""

from __future__ import annotations

import argparse
import sys
from typing import Any, Callable, Dict, Optional, Sequence, Tuple

from . import __version__
from . import boundary_double_schur_hodge
from . import horizon_schur_modular
from . import observer_sheaf_mdr
from . import padic_btz_leech
from ._canonical import canonical_digest, embed_canonical_sha256


def _count_floats(obj: Any) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(_count_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(_count_floats(v) for v in obj)
    return 0


_MODULES: Dict[str, Tuple[str, Callable[[], Dict[str, Any]]]] = {
    "horizon": (
        "AUDIT-041: Horizon Schur-Haynsworth/Krein Inertia, Pure-Q Page R_opt & Modular-Schur/GKSL Obstructions",
        horizon_schur_modular.build_certificate,
    ),
    "padic": (
        "AUDIT-042: p-Adic BTZ Holography, Delta-Y Blindness, Z_2 Holonomy Unmasking & Extremal Leech Modularity",
        padic_btz_leech.run_all,
    ),
    "mdr": (
        "AUDIT-043: 3-Term Cech-Hodge-Farkas-Tropical MDR, Aff+(1,Q)/PGL(2,Q) Tower & Lawvere-Godel Gate",
        observer_sheaf_mdr.run_all,
    ),
    "theorem": (
        "AUDIT-047: Boundary Double-Schur Holographic Hodge-1, Surgical Krein-Severing, Parallel-Sum Screening & Ramanujan 2-Lift Floor",
        boundary_double_schur_hodge.build_certificate,
    ),
}


def run_verify(module_choice: str = "all") -> Dict[str, Any]:
    if module_choice == "all":
        selected = list(_MODULES.keys())
    elif module_choice in _MODULES:
        selected = [module_choice]
    else:
        raise ValueError(f"Unknown module selector: {module_choice}")

    receipts: Dict[str, Dict[str, Any]] = {}
    for key in selected:
        desc, builder = _MODULES[key]
        payload = builder()
        _, digest = canonical_digest(payload)
        float_count = _count_floats(payload)
        if float_count != 0:
            raise RuntimeError(f"Module {key} emitted {float_count} float(s); zero floats required")
        receipts[key] = {
            "description": desc,
            "oracle_class": "exact",
            "zero_floats": True,
            "canonical_sha256": digest,
            "verified": True,
        }

    bundle: Dict[str, Any] = {
        "package": "hawking",
        "version": __version__,
        "oracle_class": "exact",
        "zero_floats": True,
        "modules_verified": len(receipts),
        "all_verified": all(r["verified"] for r in receipts.values()),
        "receipts": receipts,
    }
    embed_canonical_sha256(bundle, "bundle_sha256")
    return bundle


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="hawking",
        description="Foundation-0/hawking exact zero-float discrete horizon & holography verification suite",
    )
    parser.add_argument("--version", action="version", version=f"hawking {__version__}")
    sub = parser.add_subparsers(dest="command")

    p_ver = sub.add_parser("verify", help="Run exact pure-Q/Q(i) verification modules and emit SHA-256 receipts")
    p_ver.add_argument(
        "--module",
        choices=["all", "horizon", "padic", "mdr", "theorem"],
        default="all",
        help="Module to verify (default: all)",
    )
    p_ver.add_argument("--json", action="store_true", help="Emit canonical JSON receipt bundle to stdout")

    sub.add_parser("list", help="List available exact verification modules")

    args = parser.parse_args(argv)
    if args.command == "list":
        for key, (desc, _) in _MODULES.items():
            print(f"{key:10s}  {desc}")
        return 0

    if args.command == "verify":
        bundle = run_verify(args.module)
        if args.json:
            text, _ = canonical_digest(bundle)
            sys.stdout.write(text)
        else:
            print(f"=== Foundation-0/hawking v{__version__} Exact Zero-Float Verification ===")
            for key, info in bundle["receipts"].items():
                print(f"[PASS] {key:10s}  sha256={info['canonical_sha256'][:16]}...  {info['description']}")
            print(f"Modules verified: {bundle['modules_verified']}/{len(_MODULES) if args.module == 'all' else 1} (0 floats)")
            print(f"Bundle SHA-256:   {bundle['bundle_sha256']}")
        return 0

    parser.print_help()
    return 0
