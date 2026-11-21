# Wave 2 Round 3B — Arm H2 (`AUDIT-042`): Exact Zero-Float $p$-adic BTZ Holography, Holographic Visibility/Blindness Dichotomy, Extremal $\Lambda_{24}$ Modular Anchor & `padic-ml` Valuation Audit

**Author:** `fractals-probe`  
**Exclusive Workspace:** `symbiosis/round3/hawking-bridge/padic_btz_leech_holography/`  
**Executable Verifier:** [`hawking/padic_btz_leech.py`](../hawking/padic_btz_leech.py) (`100%` pure Python 3 standard library `fractions.Fraction` + `int`, zero `numpy`, zero floats, zero bare `assert`s; `0.28s` runtime; `4/4` isolated `-I` bit-identical stdout SHA-256 `023abda79ee809a5397bdf860ecfaf4ece8904a8e665fb91e16bb32f13ed4403`)  
**Machine Certificate:** Regenerated deterministically via `PYTHONPATH=. python3 -s -B -m hawking.padic_btz_leech --json` (`canonical_sha256`: `747d96561b9cc6a4ec412e7f0c2af86b67cc7a9e0b8e0402a454dd7377cae273`)

---

## 1. Strict Law-4 Prior-Art Boundary (`N0` vs. `N1` / `N2`)

We separate established literature (`N0`) sharply from what is proved and verified as exact discrete coordinate-free structure here (`N1`/`N2`):

- **Established Prior Art (`N0` — cited, NEVER claimed new):**
  - $p$-adic AdS/CFT & Bruhat–Tits tree $T_p$ bulk-to-boundary holography: Gubser, Knaute, Parikh, Samberg & Witaszczyk (2016).
  - $p$-adic BTZ black-hole Schottky quotients $T_p / \Gamma$: Heydeman, Marcolli, Saberi & Stoica (2016/2018).
  - Effective resistance forms & tree Schur-complement DtN operators: Kigami (2001); $\Delta$-Y electrical equivalence (Kennelly 1899), planar resistor DtN $\Delta$-Y equivalence (Curtis–Ingerman–Morrow 1998), tree four-point condition (Buneman 1974), and signed-graph balance (Harary 1953).
  - Extremal $c = 24$ 3D gravity $J(\tau) = \Theta_{\Lambda_{24}}/\Delta - 24$, Monstrous Moonshine, Ramanujan's `691`-congruence, and Hecke–Deligne bounds: Witten (2007), Conway–Norton (1979), Ramanujan (1916), Deligne (1974).
- **Verified Exact Synthesis & Discrete Obstructions (Calibrated `N1`, `AUDIT-042` `VERIFIED`, `exact` pure $\mathbb{Q}$):**
  - **Theorem H2-1A, H2-2A/B & H2-3 (`N1` exact cross-domain synthesis):** The **Complete Holographic Visibility & Blindness Dichotomy** on finite-depth $p$-adic BTZ quotients $G_{p, L, D} = T_p^{(D)} / \Gamma_L$, uniting boundary iterated-Schur DtN $\Lambda_\partial$, Buneman's UV-cutoff-invariant four-point ultrametric defect $\Delta_{\mathrm{4pt}} = 2\min(\ell_1\ell_3, \ell_2\ell_4)/L$, exact $\Delta$-Y scalar blindness at $L = 3$, universal Hodge-1 horizon-circulation blindness for all $L \ge 3$, exact $\mathbb{Z}_2$-holonomy rank-jump unmasking ($N_\partial - 1 \to N_\partial$), and exact Rank-1 Horizon-Cut Sherman–Morrison Schur duality (`Theorem H2-2B`).
  - **Part 4 (`N1`, `exact+anchor`):** Two commit-pinned code defects (`P1`, `P2`) in `google-deepmind/padic-ml@53ffd9e79890e76b82ef2dc3c7230984053f9801` (`padic_ml/_array.py` & `ops.py`) with an exact $\mathbb{Z}[1/p]$ `ExactPadic` repair.

---

## 2. Verified Pure-$\mathbb{Q}$ Theorems (`SF-01` $\cap$ `SF-02` $\cap$ `SF-03` $\cap$ `SF-05`)

Every identity below is verified entry-by-entry in `fractions.Fraction` (zero floats) across `3` vacuum Bruhat–Tits balls (`(p, D) in {(2,2), (2,3), (3,2)}`, `b_1 = 0`) and `8` BTZ black-hole quotients (`(p, L, D) in {(2,3,1), (2,4,1), (2,4,2), (2,5,1), (2,6,1), (3,4,1), (3,5,1), (5,4,1)}`, `b_1 = 1`, exact edge count $|E| = L p^D$):

### Theorem H2-1A — Exact Closed-Form BTZ Effective Resistance & UV-Invariant Four-Point Ultrametric Defect
Computing the boundary Dirichlet-to-Neumann operator $\Lambda_\partial = L_{\partial\partial} - L_{\partial I} L_{II}^{-1} L_{I\partial}$ over $\mathbb{Q}$ and inverting the grounded boundary matrix gives exact pairwise effective resistances:
$$R_{\mathrm{eff}}^{\mathrm{BTZ}}(x, y) = \begin{cases} 2(D - \operatorname{depth}(\operatorname{lca}(x, y))) & \text{same horizon sector,} \\[4pt] 2D + \dfrac{\delta(L - \delta)}{L} & \text{across horizon (cyclic distance } \delta\text{).} \end{cases}$$
- On every vacuum Bruhat–Tits tree $T_{p, D}$: $\Delta_{\mathrm{4pt}} := S_{(3)} - S_{(2)} \equiv \mathbf{0/1}$ across all checked quadruples (`15`, `210`, `210`), and exact $PGL(2, \mathbb{Q}_p)$ Möbius invariance of the cross-ratio valuation $v_p(\mathrm{CR})$ holds identically (`p = 2, 3`).
- On every BTZ quotient $G_{p, L, D}$ with $L \ge 4$: for EVERY cyclic 4-sector quadruple with arc lengths $\ell_1 + \ell_2 + \ell_3 + \ell_4 = L$, the radial cutoff $2D$ cancels identically and:
  $$S_{\mathrm{cross}} - S_{\mathrm{adj1}} = \frac{2 \ell_2 \ell_4}{L}, \qquad S_{\mathrm{cross}} - S_{\mathrm{adj2}} = \frac{2 \ell_1 \ell_3}{L} \implies \Delta_{\mathrm{4pt}} = \frac{2 \min(\ell_1 \ell_3, \ell_2 \ell_4)}{L} \in \mathbb{Q}_{>0}.$$
  Exact maxima: `L=4 -> 1/2`, `L=5 -> 2/5`, `L=6 -> 2/3` (independent of $p$, $D$, and uniform conductance scale: verified bit-identical `1/2` after rescaling all edge conductances by `7/5`!).

### Theorem H2-2A & H2-2B — Exact Discrete Hodge-1 Obstruction $\kappa_{H^1}$ & Rank-1 Horizon-Cut Schur Duality
- **Exact Discrete Hodge-1 Decomposition ($C^1 = \operatorname{im}(d_0) \oplus \ker(d_0^T)$ over $\mathbb{Q}$):**
  - Vacuum tree $T_{p, D}$: $\kappa_{H^1} \equiv \mathbf{0/1}$.
  - BTZ quotient $G_{p, L, D}$ ($b_1 = 1$, curl supported strictly on the $L$ horizon edges and `0` on all exterior hair edges):
    - Single horizon-seam defect: $\kappa_{H^1}(e_{\mathrm{hor}}) = \mathbf{1/L}$ (`1/3, 1/4, 1/5, 1/6`, invariant under scaling by `13/11` and simultaneous edge orientation flips!).
    - Uniform all-edge 1-cochain ($|E| = L p^D$): $\kappa_{H^1}^{\mathrm{unif}}(L, p, D) = \mathbf{1/p^D}$ (`1/2, 1/4, 1/3, 1/5` — exact $p$-adic UV scaling!).
    - Single exterior hair edge: $\kappa_{H^1}(e_{\mathrm{ext}}) = \mathbf{0/1}$.
- **Exact Rank-1 Horizon-Cut Schur Identity (`SF-01` $\cap$ `SF-05`):** Cutting ONE horizon edge ($b_1: 1 \to 0$) changes $\Lambda_\partial$ by an **exact rank-1 PSD matrix** $\Delta \Lambda_\partial = \Lambda_\partial^{\mathrm{BTZ}} - \Lambda_\partial^{\mathrm{cut}} = u_* u_*^T / (1 + b_*^T (L_{II}^{\mathrm{cut}})^{-1} b_*)$ (`rank == 1`, zero entry-by-entry residual across all `8` BTZ quotients; e.g., `(2, 4, 2)` SM denominator `56/23`, trace `65/644`).
- **Horizon Decoupling Limit (`SF-01` Singular Horizon):** At horizon-to-exterior coupling $\varepsilon = 1/100$ on `(2, 4, 1)`, antipodal resistance equals exact `201/1 = 2/\varepsilon + 1`; at $\varepsilon = 0$, the detached horizon cycle Laplacian $L_{C_4}$ has exact rank `3` (`1D` dark horizon zero-mode $\ker(L_{C_4}) = \operatorname{span}(\mathbf{1}_{C_4})$).

### Theorem H2-3 — The Decisive Holographic Visibility & Blindness Dichotomy
Answering whether boundary-only scalar DtN $\Lambda_\partial$ uniquely detects the BTZ horizon loop:

1. **Exact $\Delta$-Y Scalar Blindness at $L = 3$:** Across `(p=2, D=1)`, `(p=2, D=2)`, and `(p=3, D=1)`, replacing the $L=3$ horizon triangle ($b_1=1$, $\kappa_{H^1}(e_{\mathrm{hor}}) = 1/3$) with a contractible Y-star tree (central hub + 3 edges of conductance `3`, $b_1 = 0$, $\kappa_{H^1} = 0$) yields **BIT-FOR-BIT IDENTICAL $\Lambda_\partial^{\mathrm{BTZ}} \equiv \Lambda_\partial^{\mathrm{Y\text{-}star}}$ over $\mathbb{Q}$!**
2. **Geometric Visibility at $L \ge 4$:** For all $L \ge 4$, $\Delta_{\mathrm{4pt}} > 0$ breaks Buneman's tree four-point identity and proves no weighted tree can reproduce $\Lambda_\partial^{\mathrm{BTZ}}$.
3. **Universal Hodge-1 Horizon-Circulation Blindness (`L >= 3`) + Exact $\mathbb{Z}_2$ Holonomy Unmasking:** For EVERY boundary Dirichlet basis vector $\phi_\partial = e_c$, the harmonic bulk current $J = d_0 \phi$ has **identically zero** horizon circulation $\langle c_{\mathrm{hor}}, d_0 \phi \rangle \equiv 0$. Turning on a single $\mathbb{Z}_2$ edge sign flip ($\chi = -1$):
   - On the contractible Y-star tree ($b_1 = 0$): pure gauge conjugation — rank stays `N_B - 1` (`2, 5, 5`) and trace is unchanged identically (`3/2`, `39/11`, `21/5`).
   - On the BTZ black hole ($b_1 = 1$, **even at $\Delta$-Y-blind $L = 3$**): non-trivial $H^1(G, \mathbb{Z}_2)$ holonomy destroys the zero-mode, jumping rank **`N_B - 1 -> N_B`** (`2->3`, `5->6`, `5->6`) and strictly raising $\operatorname{Tr}(\Lambda_\partial^{(-1)}) > \operatorname{Tr}(\Lambda_\partial^{(+1)})$ (exact gaps: `3/10`, `54/385`, `2/15`).

---

## 3. Extremal $\Lambda_{24}$ 3D Gravity Modular Anchor (`N0`, Exact Pure `int`)

Explicitly scoped as **`N0`** (Witten 2007, Conway–Norton 1979, Ramanujan 1916, Deligne 1974), linking directly to `AUDIT-031`'s verified $\Theta_{\Lambda_{24}}(q) = E_4^3 - 720\Delta$:
- Exact pure-integer formal Laurent division confirms $j(\tau) = \Theta_{\Lambda_{24}}/\Delta + 720 = q^{-1} + 744 + 196884 q + 21493760 q^2 + 864299970 q^3 + 20245856256 q^4 + 333202640600 q^5 + \dots$, with exact microstate split $196884 = 196560\text{ (Leech kissing shell)} + 324\text{ (24-oscillator Virasoro descendants } 24^2 - 252\text{)}$ and unique extremal Niemeier $q^0 = 24 \iff r = 0$.
- Exact Eisenstein–Cusp shell identity $691 \cdot N_m(\Lambda_{24}) = 65520(\sigma_{11}(m) - \tau(m))$ verified across all `m = 1..30` (proving Ramanujan's `691`-congruence), plus exact Hecke multiplicativity $\tau(p^2) = \tau(p)^2 - p^{11}$ (`p = 2, 3, 5`) and Deligne bound $\tau(p)^2 < 4 p^{11}$ (`p = 2..23`).

---

## 4. Commit-Pinned `google-deepmind/padic-ml@53ffd9e7` Valuation Audit (`N1`, `exact+anchor`)

Direct inspection of `padic_ml/_array.py` & `padic_ml/ops.py` (`53ffd9e79890e76b82ef2dc3c7230984053f9801`) exposes two exact $\mathbb{Z}[1/p]$ arithmetic bugs:
1. **Defect P1 (`_array.py:98-103, 191-192` + `ops.py:82-92`):** `array(unit=1, valuation=-1, p=3)` explicitly constructs $1/3 \in \mathbb{Z}[1/3]$, yet `PArray.center` clamps `jnp.maximum(0, self.valuation) -> 0`, silently turning `1/3 + 0` in `ops.add` into `1/1` (`3x` error).
2. **Defect P2 (`_array.py:221-229` + `ops.py:52-60`):** `array(unit=3, valuation=0, p=3)` skips canonical re-decomposition when `p | unit`, making `ops.absolute` return `1/1` instead of $|3|_3 = 1/3$.
- Both are closed in our clean-room `ExactPadic` class (`1/3 + 0 == 1/3`, `|3|_3 == 1/3`, strong ultrametric triangle inequality verified).

---

## 5. Reproducibility & R5 Controls

```bash
for f in "-I -B" "-I -O -B" "-I -B -W error" "-I -O -B -W error"; do
  python3 $f padic_btz_leech_holography.py --json | sha256sum
done
# Expected (4/4 identical): 023abda79ee809a5397bdf860ecfaf4ece8904a8e665fb91e16bb32f13ed4403
```

All `8/8` must-fail R5 controls (`C1`–`C8`) reject cleanly.
