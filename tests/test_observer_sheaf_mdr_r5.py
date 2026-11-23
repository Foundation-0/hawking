#!/usr/bin/env python3
"""
R1-R5 Mutation-Killing Verification Suite for `observer_sheaf_mdr.py`.

Tests all exact Q linear algebra, 3-term Cech-Hodge-Farkas decomposition, Schur effective
resistance parity, exact tropical/Farkas l_inf strong duality, Aff+(1, Q)/PGL(2, Q) equalizer
tower, finite Lawvere-Godel diagonal refutation, and fail-closed boundary guards targeting
100.0% kill rate via `aletheia mutate`.

Zero bare `assert`s; R4-clean under `-I -B`, `-I -O -B`, `-I -B -W error`, `-I -O -B -W error`.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from hawking import observer_sheaf_mdr as osm  # noqa: E402


def require_cond(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError(f"TEST_FAILED: {msg}")


def expect_raises(
    exc_cls: type[BaseException],
    fn: Callable[[], Any],
    label: str,
    match: str | None = None,
) -> None:
    try:
        fn()
    except exc_cls as exc:
        if match is not None and match not in str(exc):
            raise RuntimeError(f"UNEXPECTED_MSG ({label}): {exc!r} missing {match!r}")
        return
    raise RuntimeError(f"EXPECTED_{exc_cls.__name__}_NOT_RAISED: {label}")


def run_all_tests() -> int:
    groups = 0

    # 1. Exact Q linear solver & rank-deficient orthogonal projection guards
    expect_raises(ValueError, lambda: osm._solve_exact_linear([], []), "empty linear sys", match="square")
    expect_raises(ValueError, lambda: osm._solve_exact_linear([[Fraction(1)]], []), "rhs len mismatch", match="square")
    expect_raises(
        ValueError,
        lambda: osm._solve_exact_linear([[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]], [Fraction(1), Fraction(1)]),
        "singular linear sys",
        match="singular",
    )
    sol = osm._solve_exact_linear([[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]], [Fraction(2), Fraction(7)])
    require_cond(sol == [Fraction(7), Fraction(2)], "exact pivot swap")

    # Rank-deficient column projection (dependent duplicate columns) & empty columns
    p_empty, r_empty, _, _ = osm._exact_orth_project([], [Fraction(1), Fraction(2)])
    require_cond(p_empty == [Fraction(0), Fraction(0)] and r_empty == 0, "empty cols proj")
    p_dep, r_dep, _, _ = osm._exact_orth_project(
        [[Fraction(1), Fraction(0)], [Fraction(2), Fraction(0)], [Fraction(0), Fraction(0)]],
        [Fraction(5), Fraction(9)],
    )
    require_cond(p_dep == [Fraction(5), Fraction(0)] and r_dep == 1, "dependent cols proj")
    groups += 1

    # 2. Simplicial atlas validation guards & exact 3-term Hodge-Farkas decomposition
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(1, [(0, 1)], [], [Fraction(1)]), "n_verts < 2", match="n_verts")
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(2.0, [(0, 1)], [], [Fraction(1)]), "n_verts float", match="n_verts")  # type: ignore[arg-type]
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(2, [], [], []), "empty edges", match="non-empty")
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(2, [(0, 1)], [], [Fraction(1), Fraction(2)]), "edge/weight len", match="equal length")
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(2, [(0, 1)], [], [1.0]), "float cochain", match="Fraction")  # type: ignore[list-item]
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(2, [(0, 0)], [], [Fraction(1)]), "self loop", match="bounds")
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(2, [(0, 2)], [], [Fraction(1)]), "oob endpoint", match="bounds")
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(2, [(0, 1), (1, 0)], [], [Fraction(1), Fraction(2)]), "dup undirected edge", match="duplicate")
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(3, [(0, 1), (1, 2), (0, 2)], [(0, 0, 2)], [Fraction(1)] * 3), "degenerate tri", match="invalid triangle vertices")
    expect_raises(ValueError, lambda: osm.exact_3term_hodge_farkas(3, [(0, 1), (1, 2)], [(0, 1, 2)], [Fraction(1)] * 2), "missing tri edge", match="not present")

    # Zero cochain edge case
    z_res = osm.exact_3term_hodge_farkas(2, [(0, 1)], [], [Fraction(0)])
    require_cond(z_res["global_chart_exists"] is True and z_res["fractions"]["kappa_grad"] == "0", "zero cochain")

    # Tropical n_verts > 12 guard, exact n_verts == 12 boundary, & acyclic tree (eps* == 0)
    chain_12 = [(i, i + 1) for i in range(11)]
    b12_trop = osm.exact_tropical_farkas_threshold(12, chain_12, [Fraction(1)] * 11)
    require_cond(b12_trop["eps_star_exact"] == "0", "exact n_verts == 12 boundary passes")
    chain_13 = [(i, i + 1) for i in range(12)]
    expect_raises(
        ValueError,
        lambda: osm.exact_tropical_farkas_threshold(13, chain_13, [Fraction(1)] * 12),
        "n_verts > 12 guard",
        match="<= 12",
    )
    tree_trop = osm.exact_tropical_farkas_threshold(3, [(0, 1), (1, 2)], [Fraction(5), Fraction(-2)])
    require_cond(tree_trop["eps_star_exact"] == "0" and tree_trop["strong_duality_exact_match"] is True, "acyclic tree eps*=0")

    # Mobius pole & degenerate cross-ratio guards
    expect_raises(
        ValueError,
        lambda: osm._mobius_apply((Fraction(1), Fraction(0), Fraction(1), Fraction(-2)), Fraction(2)),
        "mobius pole",
        match="pole",
    )
    expect_raises(
        ValueError,
        lambda: osm._cross_ratio(Fraction(1), Fraction(2), Fraction(3), Fraction(1)),
        "degenerate cross ratio",
        match="degenerate",
    )

    # Lawvere-Godel table validation guards
    expect_raises(ValueError, lambda: osm.verify_lawvere_diagonal_obstruction([]), "empty table", match="square")
    expect_raises(ValueError, lambda: osm.verify_lawvere_diagonal_obstruction([[1, 0]]), "non-square table", match="square")
    expect_raises(ValueError, lambda: osm.verify_lawvere_diagonal_obstruction([[1, 2], [0, 1]]), "non-binary entry", match="0 or 1")
    expect_raises(ValueError, lambda: osm.verify_lawvere_diagonal_obstruction([[True, 0], [0, 1]]), "bool entry rejected", match="0 or 1")  # type: ignore[list-item]
    groups += 1

    # 3. End-to-end exact theorem verification across all 4 atlases + tower + Lawvere-Godel
    rep = osm.run_all()
    require_cond(rep["atlas_A_regime_I_gauge_illusion"]["regime"] == "REGIME_I_GLOBAL_CHART_EXISTS", "Atlas A regime I")
    require_cond(rep["atlas_A_regime_I_gauge_illusion"]["primal_residual_max"] == "0", "Atlas A exact 0 residual")
    require_cond(rep["atlas_B_regime_II_local_contradiction"]["regime"] == "REGIME_II_LOCAL_TRIPLE_CONTRADICTION", "Atlas B regime II")
    require_cond(rep["atlas_B_regime_II_local_contradiction"]["farkas_certificate"]["certifies_infeasibility"] is True, "Atlas B Farkas cert")

    ac = rep["atlas_C_regime_III_horizon_ribbon_mdr"]
    require_cond(ac["regime"] == "REGIME_III_PURE_MDR_HORIZON_HOLONOMY", "Atlas C regime III")
    require_cond(ac["n_triangles"] == 8 and len(ac["violating_triples"]) == 0, "Atlas C 8/8 triple overlaps exact 0")
    require_cond(ac["beta_1_topological"] == 1 and Fraction(ac["fractions"]["kappa_harm"]) > 0 and ac["fractions"]["kappa_curl"] == "0", "Atlas C horizon holonomy > 0, curl == 0")
    require_cond(ac["farkas_certificate"]["certifies_infeasibility"] is True, "Atlas C harmonic Farkas cert")
    require_cond(ac["d1_d0_max_abs"] == "0" and ac["energies"]["pythagorean_residual"] == "0", "Atlas C exact chain/Pythagoras")

    acp = rep["atlas_C_pure_harmonic_core"]
    require_cond(acp["fractions"]["kappa_harm"] == "1" and acp["fractions"]["kappa_grad"] == "0" and acp["fractions"]["kappa_curl"] == "0", "Atlas C pure harmonic core kappa_harm == 1")
    peel = rep["atlas_C_multichart_cochain_peeling"]
    require_cond(peel["c_hat_max_abs_le_unit_cost"] is True and peel["homology_invariant_strict_separation"] is True, "Atlas C multichart 1-cochain peeling separation 4 > 0")

    acm = rep["atlas_C_mixed_all_three_nonzero"]
    require_cond(acm["regime"] == "REGIME_II_III_MIXED_CURL_AND_HOLONOMY", "Atlas C mixed")
    require_cond(
        Fraction(acm["fractions"]["kappa_grad"]) > 0
        and Fraction(acm["fractions"]["kappa_curl"]) > 0
        and Fraction(acm["fractions"]["kappa_harm"]) > 0,
        "Atlas C mixed all 3 > 0",
    )

    ad = rep["atlas_D_l2_hodge_vs_linf_tropical_schur"]
    require_cond(ad["c_harm_linf"] == "15/11" and ad["eps_star_tropical"] == "1", "Atlas D 15/11 > 1")
    require_cond(ad["dimensionless_l2_over_linf_ratio"] == "15/11", "Atlas D ratio 15/11")
    require_cond(ad["strict_l2_gt_linf_separation"] is True and ad["all_6_edges_schur_impulse_parity"] is True, "Atlas D Schur parity")
    require_cond(ad["tropical_farkas"]["strong_duality_exact_match"] is True, "Atlas D strong duality")
    require_cond(ad["schur_effective_resistance"]["foster_exact_match"] is True and ad["schur_effective_resistance"]["betti_exact_match"] is True, "Atlas D Foster/Betti")

    require_cond(all(rep["zero_numerology_invariance"].values()), "all zero-numerology invariances pass")
    tw = rep["observer_equalizer_tower"]
    require_cond(tw["level_0_trivial_holonomy"]["global_coordinate_glues"] is True, "Level 0 glues")
    require_cond(
        tw["level_1_translation_holonomy"]["scalar_coordinate_preserved"] is False
        and tw["level_1_translation_holonomy"]["two_point_diff_invariant_preserved"] is True,
        "Level 1 diff survives",
    )
    require_cond(
        tw["level_2_dilation_redshift_holonomy"]["two_point_diff_preserved"] is False
        and tw["level_2_dilation_redshift_holonomy"]["fixed_point_residual"] == "0"
        and tw["level_2_dilation_redshift_holonomy"]["three_point_affine_ratio_preserved"] is True
        and tw["level_2_dilation_redshift_holonomy"]["pgl2_cross_ratio_exact_invariant"] is True,
        "Level 2 fixed point + affine/cross-ratio survive",
    )
    lg = rep["lawvere_godel_sf04"]
    require_cond(lg["diagonal_obstruction"]["obstruction_holds"] is True, "Lawvere diagonal")
    require_cond(
        lg["dual_kernel_trap"]["k_bad_self_check_blind"] is True
        and lg["dual_kernel_trap"]["dual_kernel_exposes_bug"] is True
        and lg["dual_kernel_trap"]["k_bad_fails_r5_refusal"] is True
        and lg["dual_kernel_trap"]["k_exact_passes_r5_refusal"] is True,
        "SF-04 dual kernel trap",
    )
    groups += 1

    return groups


if __name__ == "__main__":
    n = run_all_tests()
    print(f"ROUND3B_OBSERVER_SHEAF_MDR_R5_OK: {n}/3 test groups passed")
