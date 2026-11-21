# Wave 2 Round 3B — Arm H3 Report: Observer-Equalizer Sheaf Gluing Dichotomy, Exact $\mathbb{Q}$ Čech–Hodge–Farkas–Tropical Obstruction & Finite Lawvere–Gödel Gate (`AUDIT-043`)

**Oracle Class:** `exact` (pure Python 3 stdlib, `fractions.Fraction` / `int` only, zero floats, zero bare `assert`s, zero external writes)  
**Honest Law-4 Novelty Classification:** **`N1`** (clean-room exact $\mathbb{Q}$ computational formalization & cross-domain unification of classical `N0` mathematical/physical foundations; **NOT** claiming a new theory of quantum gravity or rediscovery of Čech cohomology / Hodge decomposition / sheaf contextuality).

---

## 1. Strict Law-4 Prior-Art Quarantine (`N0` Foundations Explicitly Credited)

Every classical theorem and philosophical insight built upon here is explicitly quarantined as **`N0`**:

| Prior Art (`N0` — Credited, Never Overclaimed) | Role & Boundary vs. Arm H3 |
|---|---|
| **Gödel (1931), Tarski (1936), Lawvere (1969)** | Diagonal incompleteness & categorical fixed-point obstruction. We instantiate Lawvere's finite diagonal refutation directly as an executable oracle (`verify_lawvere_diagonal_obstruction`) paired with our `SF-04` acyclic dual-kernel gate. |
| **Leray (1945), Steenrod (1951), Serre (1955)** | Classical Čech cohomology $\check{H}^1(N(\mathcal{U}), G)$ and principal-bundle gluing. Simply stating *"local patches fail to glue $\iff \check{H}^1 \neq 0$"* is pure `N0`. |
| **Abramsky & Brandenburger (2011), Carù (2017), Döring & Isham (2008)** | Sheaf-theoretic contextuality via $\check{H}^1 \neq 0$ and topos-theoretic physics. Explicitly cited as `N0` prior art for sheaf-obstruction formulations of observer-dependent reality. |
| **Eckmann (1944), Jiang–Lim–Yao–Ye (2011)** | Classical 3-term discrete Hodge decomposition $C^1 = \operatorname{im}(d_0) \oplus \operatorname{im}(d_1^\top) \oplus \ker(\Delta_1)$ and HodgeRank. |
| **Farkas (1902), Foster (1949), Karp (1978)** | Linear infeasibility duality, electrical effective-resistance sum $\sum_e R_{\mathrm{eff}}(e) = |V| - \beta_0$, and minimum cycle mean duality. |
| **Hawking (2002 *Gödel and the End of Physics*), Hawking & Mlodinow (2010 *The Grand Design* — Model-Dependent Realism), Connes & Rovelli (1994), Hawking–Perry–Strominger (2016)** | Philosophical/physical framing of internal-observer incompleteness, multi-chart overlapping realism without a single global coordinate picture, thermal time, and horizon boundary degrees of freedom. |

**What Arm H3 Contributes (`N1` Executable Exact Unification):**
1. **Exact $\mathbb{Q}$ 3-Term Čech–Hodge–Farkas Atlas Dichotomy** distinguishing *Gauge/Numerology Illusion* (Regime I), *Local Triple-Overlap Contradiction* (Regime II), and *Non-Vacuous Pure Horizon-Ribbon MDR Holonomy* (Regime III, verified non-vacuously on a triangulated annulus $S^1 \times I$ with `8/8` triple overlaps satisfying $d_1 c \equiv 0$, stripping removable radial gauge `1/6` from irremovable harmonic holonomy `5/6`, plus exact harmonic Farkas infeasibility certificate $d_0^\top y = 0, y^\top c > 0$).
2. **Exact Homology-Invariant Multi-Chart 1-Cochain Peeling Separation (`H3-A` $\times$ `AUDIT-029`):** Proves that on the triangulated horizon ribbon $S^1 \times I$ with unit local step costs $w_e = 1$, EVERY global single-chart potential $d_0 s$ yields exact bound `0` on closed horizon-winding loops, whereas the multi-chart locally-consistent 1-cocycle $\hat{c} \in \ker(d_1)$ ($|\hat{c}_e| \le 1$) certifies the **exact tight topological lower bound `4 > 0`** identically across inner (`len 4`), outer (`len 4`), and triangle-deformed zig-zag (`len 6`) loops.
3. **Exact $\ell_2$-Hodge / Schur Effective Resistance vs. $\ell_\infty$-Tropical/Farkas Separation (`SF-01` $\cap$ `SF-05`):** Links unit-impulse harmonic projection identically to Schur effective resistance $c_{\mathrm{harm}}(e) \equiv 1 - R_{\mathrm{eff}}(e)$ (cross-verified by an independent exact $\mathbb{Q}$ Laplacian oracle + Foster/Betti sum `4` & `2`) and proves strict dimensionless separation $\|c_{\mathrm{harm}}\|_\infty = \mathbf{15/11} > \mathbf{1} = \epsilon^*(c) = \min_s \|c - d_0 s\|_\infty$ on an asymmetric $\theta$-graph horizon atlas (`L1=3, L2=4`), with strong minimax duality certified by exact $\mathbb{Q}$ Bellman–Ford primal potential $s^{\mathrm{LP}}$ + tight-cycle Farkas dual $y^{\mathrm{LP}}$.
4. **Exact 3-Level $\mathrm{Aff}^+(1, \mathbb{Q}) / PGL(2, \mathbb{Q})$ Observer-Equalizer Invariant Tower (`SF-07` / Session 1 Pairs 30 & 33):** Executable hierarchy showing exactly WHICH coordinate-free equalizer $\mathcal{F}^{\mathrm{inv}}$ survives as loop holonomy escalates from trivial ($A=1, B=0$: scalar $T$) $\to$ pure translation ($A=1, B=7/2$: 2-point $\Delta T$) $\to$ multiplicative dilation/redshift ($A=3/2, B=9/5$: unique horizon fixed point $t^* = -18/5$, 3-point affine ratio `3`, and 4-point $PGL(2,\mathbb{Q})$ cross-ratio `5/4`).
5. **Executable Finite Lawvere–Gödel & `SF-04` Dual-Kernel Trap:** Demonstrates finite diagonal refutation $V(d, d) \neq 1 - V(d, d)$ and an explicit float-free 53-bit truncated kernel $K_{\mathrm{bad}}$ that passes `100%` of self-consistency checks on `10^18 + 1 == 10^18` yet is exposed by BOTH acyclic dual-kernel null-equivalence and mandatory R5 refusal testing.

---

## 2. Exact Verified Rational Results (`observer_sheaf_mdr.py`)

| Construct | Exact Verified Rational Output (`Fraction`, Zero Floats) | Zero-Numerology / Invariance Verification |
|---|---|---|
| **Atlas A** (Filled 4-chart diamond, Regime I) | $\kappa_{\mathrm{grad}} = 1,\; \kappa_{\mathrm{curl}} = 0,\; \kappa_{\mathrm{harm}} = 0,\; \max |c - d_0 s| = 0$ | Exact primal chart $s = [-11/4, -5/12, -21/4, 0]$ |
| **Atlas B** (Filled diamond + perturbed overlap, Regime II) | $\kappa_{\mathrm{grad}} = 7858/8533,\; \kappa_{\mathrm{curl}} = 675/8533,\; \kappa_{\mathrm{harm}} = 0$ | Violating triple `[0,1,2]` (`defect=5`), Farkas $y^\top c = 75/8 > 0$, $d_0^\top y = 0$ |
| **Atlas C** (8-triangle annular ribbon $S^1 \times I$, Regime III) | **Raw:** $\kappa_{\mathrm{grad}}=1/6, \kappa_{\mathrm{curl}}=0, \kappa_{\mathrm{harm}}=5/6$, **`0/8` triple violations**.<br>**Harmonic core:** $\kappa_{\mathrm{harm}} = 1$.<br>**Mixed:** $\kappa_{\mathrm{grad}}=493/1176, \kappa_{\mathrm{curl}}=58/245, \kappa_{\mathrm{harm}}=289/840$ (sum $= 1$). | **Exact $S_8$ vertex perm + odd-edge flip + $\lambda = 17/11$ $\mathbb{Q}^\times$-scale invariance:** `fractions` & $\beta_1 = 1$ bit-identical! |
| **Atlas C Multi-Chart 1-Cochain Peeling** (`H3-A`) | Global single-chart $\oint d_0 s = \mathbf{0}$ on all 3 loops vs. multi-chart $\oint \hat{c} = \mathbf{4}$ on inner (`len 4`), outer (`len 4`), and zig-zag (`len 6`) loops | $|\hat{c}_e| \le 1$, $d_1 \hat{c} \equiv 0$, homology-invariant across all 8 triangles |
| **Atlas D** ($\theta$-graph `L1=3, L2=4` sharing `(0,1)`) | $\|c_{\mathrm{harm}}\|_\infty = \mathbf{15/11} > \mathbf{1} = \epsilon^*(c)$; $R_{\mathrm{eff}} = [6/11, 7/11, 7/11, 8/11, 8/11, 8/11]$; Foster sum $= 4$, $\sum(1 - R_{\mathrm{eff}}) = 2 = \beta_1$ | `6/6` edges satisfy $c_{\mathrm{harm}}(e) \equiv 1 - R_{\mathrm{eff}}(e)$; strong duality `primal == dual == 1`; ratio `15/11` invariant under $\lambda = 13/7$ |
| **Equalizer Tower** ($\mathrm{Aff}^+(1,\mathbb{Q}) / PGL(2,\mathbb{Q})$) | Lvl 0: $(A,B)=(1,0)$ glues; Lvl 1: $(1, 7/2)$ preserves $\Delta T$; Lvl 2: $(3/2, 9/5)$ unique fixed point $t^* = -18/5$ (`res=0`), affine ratio `3`, $PGL(2)$ cross-ratio `5/4` | Exact `0` residual across both loop monodromy and non-affine Möbius transform `(3z+5)/(2z+7)` |
| **Lawvere–Gödel & `SF-04` Trap** | `4x4` diagonal refutation `0` representing rows; 53-bit `K_bad` blind to `10^18+1 == 10^18`, exposed by exact dual kernel & R5 | Zero-float bitwise exact model of IEEE-754 truncation |

---

## 3. Repro Commands, Verified Receipts & Falsification Criteria

Run from `symbiosis/round3/hawking-bridge/observer_sheaf_mdr/`:

```bash
for m in "-I -B" "-I -O -B" "-I -B -W error" "-I -O -B -W error"; do
  python3 $m observer_sheaf_mdr.py --json | sha256sum
  python3 $m test_observer_sheaf_mdr_r5.py
done

PYTHONPATH=../../../../publish/aletheia python3 -B -W error -m aletheia mutate observer_sheaf_mdr.py \
  --test-cmd "python3 test_observer_sheaf_mdr_r5.py" --work-root . --json

PYTHONPATH=../../../../publish/aletheia python3 -B -W error -m aletheia audit-check . \
  --scripts observer_sheaf_mdr.py test_observer_sheaf_mdr_r5.py --json
```

**Verified Receipts:**
- `observer_sheaf_mdr.py --json`: `4/4` isolated `-I` R4 bit-identical SHA-256 `4381de1226f3bf2f65f5e8a74cebee03177d236391d0b3db5790fb4dce632a1d`
- `aletheia mutate observer_sheaf_mdr.py`: **`18/18 = 100.0%` KILLED, `0` survivors**
- `aletheia audit-check`: **`PASS`** (`3` files, `0` CRLF, `0` `__pycache__`, `0` leaks, `0` bare `assert`s, `2/2` isolated R4 scripts bit-identical)

**Falsification Criteria:**
- Falsified if ANY chain-complex axiom ($d_1 d_0 = 0$), orthogonality dot product, Pythagorean residual, harmonic conservation ($d_0^\top c_{\mathrm{harm}} = 0, d_1 c_{\mathrm{harm}} = 0$), Farkas certificate, Schur/Foster identity, Bellman–Ford strong duality, or equalizer residual is non-zero;
- Falsified if ANY zero-numerology invariance check ($S_8$ perm + edge flips + $\mathbb{Q}^\times$ scaling, Möbius cross-ratio) deviates from exact equality;
- Falsified if ANY mutant survives `aletheia mutate` (`18/18`), or ANY script fails 4-mode isolated R4 parity / `aletheia audit-check`.
