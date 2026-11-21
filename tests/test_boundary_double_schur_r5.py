#!/usr/bin/env python3
"""Clean-room R5 mutation & negative-control test suite for
boundary_double_schur_hodge_theorem.py (100% pure Python 3 stdlib, zero bare asserts).
"""

from __future__ import annotations

import sys
import unittest
from fractions import Fraction
from pathlib import Path

_ROOT = str(Path(__file__).resolve().parent.parent)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from hawking import boundary_double_schur_hodge as bd


class TestBoundaryDoubleSchurHodgeR5(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = bd.build_certificate()

    def test_01_r3_strict_rejections(self) -> None:
        res = self.cert["r3_negative_controls"]
        self.assertTrue(res["all_r3_rejected"])
        self.assertEqual(res["count"], 12)
        with self.assertRaises(TypeError):
            bd.exact_frac(False)
        with self.assertRaises(TypeError):
            bd.exact_frac("1/2")
        with self.assertRaisesRegex(ZeroDivisionError, r"Q\(i\)"):
            _ = bd.G1 / bd.G0
        with self.assertRaises(ValueError):
            bd.validate_graph(1, [], [0])
        with self.assertRaises(ValueError):
            bd.validate_graph(True, [], [0])
        with self.assertRaises(ValueError):
            bd.validate_graph(2, [(0, 1, Fraction(1))], [2])
        with self.assertRaises(ValueError):
            bd.validate_graph(2, [(0, 1, Fraction(1))], [True])
        with self.assertRaises(TypeError):
            bd.validate_graph(2, [(True, 1, Fraction(1))], [0])
        with self.assertRaises(ValueError):
            bd.validate_graph(2, [(0, 1, Fraction(-1))], [0])
        with self.assertRaises(ValueError):
            bd.validate_graph(2, [(0, 5, Fraction(1))], [0])
        with self.assertRaises(ValueError):
            bd.mat_mul_q([[Fraction(1)]], [[Fraction(1)], [Fraction(2)]])
        with self.assertRaises(ValueError):
            bd.invert_q([])
        with self.assertRaises(ValueError):
            bd.invert_q([[Fraction(1), Fraction(2)]])
        with self.assertRaisesRegex(ValueError, "Singular"):
            bd.invert_q([[Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)]])
        with self.assertRaises(ValueError):
            bd.invert_qi([])
        with self.assertRaisesRegex(ValueError, "Singular"):
            bd.invert_qi([[bd.G1, bd.G1], [bd.G1, bd.G1]])
        with self.assertRaises(ValueError):
            bd.det_q([])
        with self.assertRaisesRegex(ValueError, "length"):
            bd.exact_hodge1_decomposition(2, [(0, 1, Fraction(1))], [Fraction(1), Fraction(2)])
        with self.assertRaisesRegex(ValueError, "length"):
            bd.boundary_double_schur_holonomy(2, [(0, 1, Fraction(1))], [0], [Fraction(1), Fraction(2)])
        with self.assertRaisesRegex(ValueError, "length"):
            bd.finite_t_magnetic_dtn_energy(2, [(0, 1, Fraction(1))], [0], [Fraction(1), Fraction(2)], Fraction(1))
        with self.assertRaisesRegex(ValueError, "length"):
            bd.signed_dtn_q(2, [(0, 1, Fraction(1))], [0], [1, 1])
        with self.assertRaises(ValueError):
            bd.signed_dtn_q(2, [(0, 1, Fraction(1))], [0], [True])
        with self.assertRaisesRegex(ValueError, "unit weights"):
            bd.verify_ramanujan_monopole_floor("bad_w", 2, [(0, 1, Fraction(2))], [0], [1], 1, True, True)
        with self.assertRaisesRegex(ValueError, "regular"):
            bd.verify_ramanujan_monopole_floor("bad_deg", 3, [(0, 1, Fraction(1)), (1, 2, Fraction(1))], [0], [1, 1], 2, True, True)
        with self.assertRaises(RuntimeError):
            bd.verify_certificate_integrity({})
        # Exercise symmetric_inertia_q edge cases (empty, zero column, hyperbolic pivot swap, 4x4 trailing update)
        self.assertEqual(bd.symmetric_inertia_q([]), (0, 0, 0))
        self.assertEqual(bd.symmetric_inertia_q([[Fraction(0)]]), (0, 1, 0))
        self.assertEqual(
            bd.symmetric_inertia_q([
                [Fraction(0), Fraction(0), Fraction(2)],
                [Fraction(0), Fraction(0), Fraction(0)],
                [Fraction(2), Fraction(0), Fraction(3)],
            ]),
            (1, 1, 1),
        )
        self.assertEqual(
            bd.symmetric_inertia_q([
                [Fraction(0), Fraction(1), Fraction(2), Fraction(0)],
                [Fraction(1), Fraction(2), Fraction(1), Fraction(1)],
                [Fraction(2), Fraction(1), Fraction(5), Fraction(0)],
                [Fraction(0), Fraction(1), Fraction(0), Fraction(-1)],
            ]),
            (2, 0, 2),
        )

    def test_02_exact_double_schur_identity_and_period_rank(self) -> None:
        p1 = self.cert["part1_boundary_double_schur_hodge_and_period_recovery"]
        self.assertTrue(p1["all_hodge_and_double_schur_identities_verified"])
        self.assertEqual(len(p1["families_verified"]), 7)
        self.assertTrue(p1["delta_Y_scalar_Lam0_identical_yet_H_partial_separates_1_3_vs_0"])
        self.assertTrue(p1["pure_harmonic_first_order_blind_second_order_exact"])
        edges = [(0, 1, Fraction(2)), (1, 2, Fraction(3)), (2, 3, Fraction(5)), (3, 0, Fraction(7))]
        c = [Fraction(1), Fraction(-2), Fraction(4), Fraction(3)]
        h_ref = bd.exact_hodge1_decomposition(4, edges, c)["harm_norm2"]
        self.assertEqual(h_ref, Fraction(7560, 247))
        for bnd in [[0], [1, 3], [0, 1, 2, 3]]:
            res = bd.boundary_double_schur_holonomy(4, edges, bnd, c)
            self.assertEqual(res["H_partial"], h_ref)

    def test_03_parallel_sum_screening_and_noncommuting_limits(self) -> None:
        p2 = self.cert["part2_parallel_sum_horizon_screening_and_noncommuting_limits"]
        self.assertEqual(len(p2["symmetric_horizon_exact_parallel_sum_rows"]), 18)
        self.assertEqual(len(p2["asymmetric_theta_horizon_screening_rows"]), 6)
        self.assertTrue(p2["non_commuting_decoupling_obstruction"]["discontinuous_jump_verified"])
        e3 = [(0, 1, Fraction(1)), (1, 2, Fraction(1)), (2, 0, Fraction(1))]
        c3 = [Fraction(1), Fraction(1), Fraction(1)]
        val = bd.finite_t_magnetic_dtn_energy(3, e3, [0, 1, 2], c3, Fraction(1))
        self.assertEqual(val, Fraction(6))

    def test_04_surgical_edge_severing_and_krein_trichotomy(self) -> None:
        p3 = self.cert["part3_surgical_edge_severing_and_krein_inertia_trichotomy"]
        self.assertEqual(len(p3["single_edge_surgical_and_krein_trichotomy_cases"]), 12)
        self.assertTrue(p3["k4_naive_1B_perp_restriction_counterexample_verified"])
        self.assertEqual(len(p3["multi_edge_psd_variance_cases"]), 3)
        e3 = [(0, 1, Fraction(2)), (1, 2, Fraction(3)), (2, 0, Fraction(5))]
        res = bd.verify_single_edge_surgical_krein("K3_full_bnd", 3, e3, [0, 1, 2], 0, "case_I_observable_krein_split")
        self.assertTrue(res["trichotomy_exact_match"])
        self.assertTrue(res["surgical_severing_Lam_red_eq_Lam_cut"])
        self.assertEqual(res["inertia_Delta_full"], [1, 1, 1])
        self.assertEqual(res["Phi_B_exact"], "8")
        lam_p = bd.signed_dtn_q(3, e3, [0, 1, 2], [1, 1, 1])
        red, phi = bd.monopole_reduced_dtn_q(lam_p)
        self.assertEqual(phi, Fraction(0))
        self.assertEqual(red, lam_p)

    def test_05_signed_2lift_splitting_and_ramanujan_floor(self) -> None:
        p4 = self.cert["part4_signed_2lift_deck_splitting_and_ramanujan_floor"]
        self.assertEqual(len(p4["deck_splitting_cases_verified"]), 6)
        self.assertEqual(len(p4["ramanujan_monopole_floor_cases"]), 7)
        self.assertTrue(p4["boundary_ramanujan_falsifier_529_gt_512_verified"])
        e3 = [(0, 1, Fraction(1)), (1, 2, Fraction(1)), (2, 0, Fraction(1))]
        lam_s = bd.signed_dtn_q(3, e3, [0, 1, 2], [-1, 1, 1])
        self.assertEqual(bd.rank_q(lam_s), 3)
        self.assertEqual(bd.det_q(lam_s), Fraction(4))
        self.assertEqual(bd.rank_q([]), 0)
        self.assertEqual(-bd.G1, bd.GaussQ(-1, 0))
        self.assertFalse(bd.G1 == True)
        self.assertFalse(bd.G1 == "1")
        self.assertTrue(bd.G1 == 1)

    def test_06_full_certificate_build(self) -> None:
        self.assertTrue(self.cert["zero_floats_pure_Q_Qi"])
        self.assertEqual(self.cert["oracle_class"], "exact")


if __name__ == "__main__":
    unittest.main()
