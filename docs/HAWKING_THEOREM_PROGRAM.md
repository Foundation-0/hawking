# Round 4 — Arm R4-4: The Boundary Double-Schur Holographic Hodge-1, Surgical Krein-Severing, Parallel-Sum Horizon-Screening & Ramanujan 2-Lift Theorem (`AUDIT-047`)

- **Owner:** `gravity-probe` (Arm R4-4, `#263` Deliverable 2 + `#264` Portal `R4-P04` / `SF-01 #18`)
- **Workspace:** `symbiosis/round4/hawking-theorem/`
- **Artifacts:** `boundary_double_schur_hodge_theorem.py`, `test_hawking_theorem_r5.py`, `boundary_double_schur_hodge_certificate.json`, `HAWKING_THEOREM_PROGRAM_REPORT.md`
- **Oracle Class:** `exact` (**100% pure Python 3 stdlib `fractions.Fraction` & $\mathbb{Q}[i]$, ZERO floats anywhere**)
- **Naming Restraint & Law-4 Honesty (`#263` Strict Rule):** We name this theorem strictly by its exact mathematical content — **The Boundary Double-Schur Holographic Hodge-1, Surgical Krein-Severing & Parallel-Sum Horizon-Screening Theorem** — and explicitly submit it to `@verifier` (`AUDIT-047`) for independent `N1` vs `N2` adjudication rather than prematurely calling it "The Hawking Theorem." We isolate the 3 exact mathematical barriers remaining between this universal finite-graph holographic theorem and continuum Lorentzian quantum gravity.

---

## 1. Strict Law-4 `N0` Prior-Art Quarantine (Enforcing `R4-N0-06`–`R4-N0-11`)

No classical or modern result below is claimed as `N1` or `N2`:

| Prior Art (`N0` — Explicitly Credited, Never Claimed New) | Exact Scope & Sharp Delta vs. Our 4-Part Theorem |
|---|---|
| **Schur (1917); Sylvester (1852); Haynsworth (1968); Albert (1969)** | Matrix Schur complements, Dirichlet variational principle, inertia additivity, PSD range conditions. |
| **Kirchhoff (1847); Foster (1948); Kennelly (1899); Curtis–Ingerman–Morrow (1998)** | Untwisted electrical DtN response $\Lambda_\partial$, $\Delta$-Y electrical equivalence, $R_{\mathrm{eff}}(e)$, $c_{\mathrm{harm}}(e) = 1 - w_e R_{\mathrm{eff}}(e)$. |
| **Farkas (1902); Eckmann (1944); Harary (1953); Zaslavsky (1982)** | Linear infeasibility duality, discrete Hodge decomposition $C^1 = \operatorname{im}(d_0) \oplus \ker(d_0^\top W)$, and unbalanced signed-graph invertibility ($\ker(L^{(\chi)}) = 0 \implies \operatorname{rank}(\Lambda_B(\chi)) = |B|$ via Haynsworth). |
| **Forman (1993); Kenyon (2011)** | Cycle-rooted spanning forest (CRSF) determinant formula $\det(L^{(\chi)})$ and circular-planar bundle DtN maps. |
| **Bilu–Linial (2006); Marcus–Spielman–Srivastava (2015)** | Full-graph signed 2-lift spectrum decomposition $\operatorname{Spec}(\tilde L_\sigma) = \operatorname{Spec}(L^{(+1)}) \sqcup \operatorname{Spec}(L^{(\sigma)})$ and existence of Ramanujan 2-lifts. |
| **Berkolaiko–Kuchment (2013); Sunada (2013); Lange–Liu–Peyerimhoff–Post (2015)** | Full-graph ($\partial = V$) magnetic Laplacian diamagnetic ground-state stiffness $\frac{1}{|V|}\|\Pi_{H^1} c\|_W^2$. |
| **Hawking (1974/76/2002/2010); Page (1993); Takesaki (1972); Connes–Rovelli (1994)** | Physical motivation (horizon information, Page min-switch, MDR, modular flow). |

**What Is Strictly Beyond `R4-N0-06`–`R4-N0-11`:**
1. **Part 1:** Boundary-independent **double-Schur** identity $\mathcal{H}_\partial(c) \equiv \|\Pi_{H^1} c\|_W^2$ recovering the entire $\beta_1(G)$-rank bulk Hodge-1 period Gram matrix strictly from a **single observer vertex** $|\partial| = 1$ (breaking $\Delta$-Y electrical blindness identically).
2. **Part 2:** Exact finite-$(t,\varepsilon)$ **parallel-sum horizon-screening inequality** $\mathbf{1}_\partial^\top \Lambda_\partial(t,\varepsilon)\mathbf{1}_\partial \le \frac{C_{\mathrm{cut}}\mathcal{E}_{\mathrm{hol}}}{C_{\mathrm{cut}}+\mathcal{E}_{\mathrm{hol}}}$ (exact equality on vertex-transitive rings) forcing **non-commuting probe/detachment limits** linked directly to `AUDIT-041`'s singular kernel $\ker(L_{II}) \neq 0$.
3. **Part 3 (Resolving `R4-P04` Candidate `N2-A` / `SF-01 #18`):** The **Universal Surgical Edge-Severing Identity** $\Lambda_B^{\mathrm{red}}(\chi_{e^*}) \equiv \Lambda_B^{(G\setminus\{e^*\})}(1) = \Lambda_B^{(G)}(1) - \frac{w_{e^*}}{c_{\mathrm{harm}}^{(B)}(e^*)}(h_u - h_v)(h_u - h_v)^\top$, the **exact 3-way Krein inertia trichotomy** $(1, |B|-2, 1)$ / $(1, |B|-1, 0)$ / $(0, |B|, 0)$ of $\Delta\Lambda_B(\chi_{e^*})$, the **exact falsification of the naive $\mathbf{1}_B^\perp$-restriction conjecture** on weighted $K_4$, and the **multi-edge PSD variance bound** $\Lambda_B^{\mathrm{red}}(\chi_F) \succeq \Lambda_B^{(G\setminus F)}(1)$.
4. **Part 4 (Bridging `R4-1` ↔ `R4-4`):** Exact $\mathbb{Q}$-orthogonal deck splitting $M_{\mathrm{deck}}^\top \tilde\Lambda_{\tilde B} M_{\mathrm{deck}} \equiv 2(\Lambda_B^{(+1)} \oplus \Lambda_B^{(\sigma)})$ paired with the **square-root-free Ramanujan 2-lift monopole spectral floor** $\Phi_B(\chi)/|B| \ge d - 2\sqrt{d-1}$ AND its contrapositive **boundary Ramanujan falsifier** (explicitly witnessing $529/64 > 8$ on a 12-vertex 3-regular non-Ramanujan lift strictly from boundary monopole response!).

---

## 2. Main Unified Theorem (Complete Proof over Pure $\mathbb{Q}$ and $\mathbb{Q}[i]$)

Let $G = (V, E, w)$ be **any** finite connected positive-weighted graph ($w_e \in \mathbb{Q}_{>0}$), $B = \partial \subseteq V$ **any** non-empty boundary subset (down to $|B| = 1$), $I = V \setminus B$ the hidden bulk interior, and $h_x \in \mathbb{Q}^{|B|}$ the untwisted boundary harmonic-measure vector of vertex $x$ ($h_x = e_x$ for $x \in B$; $H_I = -L_{II}^{-1} L_{IB}$).

### Part 1: Boundary Double-Schur Holographic Hodge-1 & $|\partial| = 1$ Period-Matrix Recovery (`AUDIT-042` $\cap$ `AUDIT-043`)
Equip $G$ with any 1-cochain $c \in C^1(E, \mathbb{Q})$ and exact rational unit-modulus Cayley $U(1)$ connection $u_e(t) = \frac{1 + i t c_e}{1 - i t c_e} \in \mathbb{Q}(i, t)$. Expand the boundary Dirichlet-to-Neumann Schur complement
$$\Lambda_\partial(t) := L_{\partial\partial}(t) - L_{\partial I}(t)\,L_{II}(t)^{-1}\,L_{I\partial}(t) \;=\; \Lambda_0 + i t \Lambda_1 + t^2 \Lambda_2 + O(t^3)$$
and define the **Boundary Double-Schur Holonomy Invariant** (eliminating both interior $I$ and boundary gauge $\operatorname{im}(\Lambda_0)$):
$$\mathcal{H}_\partial(c) \;:=\; \frac{1}{4}\Bigl(\mathbf{1}_\partial^\top \Lambda_2 \mathbf{1}_\partial \;-\; (\Lambda_1 \mathbf{1}_\partial)^\top \Lambda_0^+ (\Lambda_1 \mathbf{1}_\partial)\Bigr) \;\in\; \mathbb{Q}_{\ge 0}.$$
Then for **every** connected $G = (V, E, w)$, **every** non-empty $\partial \subseteq V$ (including $|\partial| = 1$), and **every** $c \in C^1(E, \mathbb{Q})$:
1. $\mathcal{H}_\partial(c) \equiv \|\Pi_{\ker(d_0^\top W)} c\|_W^2 = \|c\|_W^2 \kappa_{H^1}(c)$.
2. **First-order harmonic blindness:** If $d_0^\top W c = 0$, then $\Lambda_1 \mathbf{1}_\partial \equiv 0$, yet $\frac{1}{4}\mathbf{1}_\partial^\top \Lambda_2 \mathbf{1}_\partial = \|c\|_W^2$.
3. **Full bulk genus recovery at $|\partial| = 1$:** Polarizing $\mathcal{H}_\partial$ at a single observer vertex reconstructs the exact bulk Hodge-1 period Gram matrix of rank $\beta_1(G)$ — separating $\Delta$-Y-identical scalar graphs (`BTZ L = 3` vs `Y-star`: identical $\Lambda_0$, yet $\mathcal{H}_\partial = 1/3$ vs `0`, period rank `1` vs `0`).
4. **Farkas global-chart witness (`AUDIT-043`):** $\mathcal{H}_\partial(c) = 0 \iff c \in \operatorname{im}(d_0)$; whenever $\mathcal{H}_\partial(c) > 0$, $y = W \Pi_{H^1} c$ satisfies $d_0^\top y = 0$ and $y^\top c = \mathcal{H}_\partial(c) > 0$.

### Part 2: Exact Finite-$(t, \varepsilon)$ Parallel-Sum Horizon-Screening Inequality & Non-Commuting Limits (`AUDIT-041` $\cap$ `AUDIT-042`)
If an interior horizon $H \subset I$ connects to $V \setminus H$ across total cut conductance $C_{\mathrm{cut}}(\varepsilon) = \sum_{e \in \partial H} w_e = O(\varepsilon)$ with $c$ supported on $H$ and raw holonomy energy $\mathcal{E}_{\mathrm{hol}}(t) := \sum_{e \in E(H)} w_e \frac{4 t^2 c_e^2}{1 + t^2 c_e^2}$, then for **every** $t \in \mathbb{Q}$ and $\varepsilon > 0$:
$$\mathbf{1}_\partial^\top \Lambda_\partial(t, \varepsilon)\,\mathbf{1}_\partial \;\le\; \frac{C_{\mathrm{cut}}(\varepsilon)\,\mathcal{E}_{\mathrm{hol}}(t)}{C_{\mathrm{cut}}(\varepsilon) + \mathcal{E}_{\mathrm{hol}}(t)} \;\le\; \min\!\bigl(C_{\mathrm{cut}}(\varepsilon),\ \mathcal{E}_{\mathrm{hol}}(t)\bigr),$$
with **exact equality** on vertex-transitive horizons ($C_L$, 18/18 triples verified), forcing **non-commuting decoupling limits**:
$$\lim_{\varepsilon \to 0^+}\,\lim_{t \to 0}\,\frac{\mathcal{E}_\partial(t, \varepsilon)}{4 t^2} \;=\; \|\Pi_{H^1(H)} c\|_W^2 \;>\; 0 \;\neq\; 0 \;=\; \lim_{t \to 0}\,\lim_{\varepsilon \to 0^+}\,\frac{\mathcal{E}_\partial(t, \varepsilon)}{4 t^2}.$$

### Part 3: Universal Surgical Edge-Severing Identity, Rank-2 Krein-Woodbury Monopole Law & Exact Krein Inertia Trichotomy (`AUDIT-041` $\cap$ `AUDIT-042` $\cap$ `AUDIT-043`, Resolving `R4-P04` / `SF-01 #18`)
For **any** $\mathbb{Z}_2$ signing $\chi_F \in \{\pm 1\}^E$ flipping edge set $F \subset E$, define the observer difference $\Delta\Lambda_B(\chi_F) := \Lambda_B(\chi_F) - \Lambda_B(1)$, monopole unmasking $\Phi_B(\chi_F) := \mathbf{1}_B^\top \Lambda_B(\chi_F)\mathbf{1}_B$, and **monopole-eliminated Schur complement**:
$$\Lambda_B^{\mathrm{red}}(\chi_F) \;:=\; \Lambda_B(\chi_F) \;-\; \frac{\bigl(\Lambda_B(\chi_F)\mathbf{1}_B\bigr)\bigl(\Lambda_B(\chi_F)\mathbf{1}_B\bigr)^\top}{\Phi_B(\chi_F)}.$$
For any edge $e^* = (u, v) \in E$, let $R_{\mathrm{eff}}^{(B)}(e^*)$ be its Dirichlet-grounded effective resistance in $G/B$ and $c_{\mathrm{harm}}^{(B)}(e^*) := 1 - w_{e^*} R_{\mathrm{eff}}^{(B)}(e^*) \in [0, 1]$ its boundary-relative Hodge-1 harmonic energy.
1. **Universal Surgical Edge-Severing Identity (ALL edges $e^* \in E$ — interior, collar, or boundary — with $c_{\mathrm{harm}}^{(B)}(e^*) > 0$):**
   $$\Lambda_B^{\mathrm{red}}(\chi_{e^*}) \;\equiv\; \Lambda_B^{(G \setminus \{e^*\})}(1) \;=\; \Lambda_B^{(G)}(1) \;-\; \frac{w_{e^*}}{c_{\mathrm{harm}}^{(B)}(e^*)}\,(h_u - h_v)(h_u - h_v)^\top.$$
   Flipping a *single* bulk edge's $\mathbb{Z}_2$ sign and taking the monopole Schur complement on $B$ **surgically deletes $e^*$ from the hidden bulk**.
2. **Exact Two-Term Krein Decomposition & Universal Inertia Trichotomy:** Writing $v := \Lambda_B(\chi_{e^*})\mathbf{1}_B$ ($v^\top \mathbf{1}_B = \Phi_B > 0$) and $\Delta h_{e^*} := h_u - h_v \in \mathbf{1}_B^\perp$:
   $$\Delta\Lambda_B(\chi_{e^*}) \;=\; +\frac{1}{\Phi_B}\, v v^\top \;-\; \frac{w_{e^*}}{c_{\mathrm{harm}}^{(B)}(e^*)}\,\Delta h_{e^*}\Delta h_{e^*}^\top,$$
   giving the exact necessary-and-sufficient 3-way Krein signature classification:
   $$\operatorname{inertia}\!\bigl(\Delta\Lambda_B(\chi_{e^*})\bigr) \;=\; \begin{cases} (1,\ |B|-2,\ 1) & \iff h_u \neq h_v \text{ (harmonic-observable flip: exact }(1,1)\text{ Krein split)}, \\ (1,\ |B|-1,\ 0) & \iff h_u = h_v \text{ and } c_{\mathrm{harm}}^{(B)}(e^*) > 0 \text{ (boundary-symmetry-blind cycle: pure rank-1 PSD)}, \\ (0,\ |B|,\ 0) & \iff c_{\mathrm{harm}}^{(B)}(e^*) = 0 \text{ (dead-end bridge: exact trivial coboundary }\Delta\Lambda_B \equiv 0\text{)}. \end{cases}$$
   For every interior flip $e^* = (u, v) \in E(I)$, $\Phi_B(\chi_{e^*})$ satisfies the **exact rank-2 Krein-Woodbury rational law**:
   $$\Phi_B(\chi_{e^*}) \;=\; \frac{4\,w_{e^*}^{-1}\,c_{\mathrm{harm}}^{(B)}(e^*)}{\bigl(w_{e^*}^{-1} + (e_u+e_v)^\top L_{II}^{-1}(e_u+e_v)\bigr)\,w_{e^*}^{-1}c_{\mathrm{harm}}^{(B)}(e^*) + \bigl((L_{II}^{-1})_{uu} - (L_{II}^{-1})_{vv}\bigr)^2}.$$
   - **Falsification of Naive $\mathbf{1}_B^\perp$-Restriction Hypothesis (Weighted $K_4$ Catch):** On weighted $K_4$ ($w = 1..6$, $B = \{0,1\}$, interior flip $e^* = (2,3)$), full $\Delta\Lambda_B$ has Krein inertia $(1, 0, 1)$, **yet the orthogonal restriction $\Delta\Lambda_B|_{\mathbf{1}_B^\perp}$ has inertia $(1, 0, 0)$ (strictly positive!)** because the unique negative Krein eigenvector tilts across $\mathbf{1}_B \oplus \mathbf{1}_B^\perp$. The universal negative mode lives strictly on the **monopole-eliminated Schur complement** $\Lambda_B^{\mathrm{red}} - \Lambda_B(1) \preceq 0$, NOT on $\Delta\Lambda_B|_{\mathbf{1}_B^\perp}$.
3. **Multi-Edge PSD Variance Bound (`|F| >= 1`):** For any flip set $F \subset E$ with invertible $L_{II}^{(G\setminus F)}$, $\Lambda_B^{\mathrm{red}}(\chi_F) \succeq \Lambda_B^{(G\setminus F)}(1)$ identically as PSD matrices, with gap rank $\le |F| - 1$ (zero iff $|F| = 1$ or constant midpoint harmonic potential).

### Part 4: Universal Signed 2-Lift Deck Splitting & Pure-$\mathbb{Q}$ Ramanujan Monopole Spectral Floor (`AUDIT-042` $\cap$ `R4-1`)
1. **Exact Deck-Basis Splitting:** On the 2-lift $\tilde G_\sigma$ with lifted boundary $\tilde B = B_+ \sqcup B_-$ and deck matrix $M_{\mathrm{deck}} = \begin{pmatrix} I & I \\ I & -I \end{pmatrix}$,
   $$M_{\mathrm{deck}}^\top\,\tilde{\Lambda}_{\tilde B}\,M_{\mathrm{deck}} \;\equiv\; 2\,\bigl(\Lambda_B^{(+1)} \oplus \Lambda_B^{(\sigma)}\bigr)$$
   identically over $\mathbb{Q}$, with $\operatorname{rank}(\Lambda_B^{(\sigma)}) = |B| \iff \det(\Lambda_B^{(\sigma)}) > 0 \iff \Phi_B(\sigma) > 0 \iff [\sigma] \neq 0 \in H^1(G, \mathbb{Z}_2)$. *(Note: $\operatorname{tr}(\Delta\Lambda_B)$ need NOT be positive — weighted $K_4$ boundary flip `(0,1)` gives exact $\Delta\operatorname{Tr} = 0$ while $\Phi_B = 4 > 0$!)*
2. **Exact Square-Root-Free Ramanujan Monopole Spectral Floor & Boundary Falsifier:** For **any** $d$-regular unit-weight graph $G$ and **any** Bareiss-certified Ramanujan signed 2-lift $(G, \chi)$ ($4(d-1)I - A_\chi^2 \succeq 0$, verified with zero floats via `symmetric_inertia_q`), every non-empty boundary $B \subset V$ satisfies:
   $$\frac{\Phi_B(\chi)}{|B|} \ge d \quad \text{or} \quad \left(d - \frac{\Phi_B(\chi)}{|B|}\right)^2 \le 4(d-1), \qquad \Phi_B(\chi) \le w(B, I) + 4 w(F \cap E(B)).$$
   **Contrapositive Boundary Ramanujan Falsifier:** If an observer on $B$ measures $\Phi_B(\chi)/|B| < d$ with $(d - \Phi_B(\chi)/|B|)^2 > 4(d-1)$, the hidden bulk 2-lift is **guaranteed non-Ramanujan** strictly from boundary monopole response! Explicitly witnessed on a 12-vertex 3-regular ladder-dumbbell (`|B| = 4`): $\Phi_B/|B| = 1/8 \implies (3 - 1/8)^2 = 529/64 > 8$ (`529 > 512`), independently confirmed by $n_-(8I - A_\chi^2) = 1$.

### Concise Proofs
- **Part 1:** By Schur's variational principle, $\min_{\alpha_\partial} (\mathbf{1}_\partial + i t \alpha_\partial)^\dagger \Lambda_\partial(t)(\mathbf{1}_\partial + i t \alpha_\partial) = \min_{f \in \mathbb{R}^V} (\mathbf{1}_V + i t f)^\dagger L(t)(\mathbf{1}_V + i t f)$. Expanding both sides to exact order $t^2$ yields $4 t^2 \mathcal{H}_\partial(c)$ on the LHS and $t^2 \min_f \|d_0 f - 2 c\|_W^2 = 4 t^2 \|\Pi_{\ker(d_0^\top W)} c\|_W^2$ on the RHS.
- **Part 2:** Restricting $\min_{\phi|_\partial = \mathbf{1}_\partial} \phi^\dagger L(t) \phi$ to $\phi|_{V \setminus H} \equiv 1$, $\phi|_H \equiv z \in \mathbb{C}$ yields $\min_z(C_{\mathrm{cut}}|1-z|^2 + \mathcal{E}_{\mathrm{hol}}|z|^2) = \frac{C_{\mathrm{cut}}\mathcal{E}_{\mathrm{hol}}}{C_{\mathrm{cut}}+\mathcal{E}_{\mathrm{hol}}}$.
- **Part 3:** For any $\psi_B \in \mathbb{R}^{|B|}$, $\psi_B^\top \Lambda_B^{\mathrm{red}}(\chi_F)\psi_B = \min_{\alpha \in \mathbb{R},\,\phi|_B = \psi_B} \bigl[\sum_{e \notin F} w_e(\phi_x - \phi_y)^2 + \sum_{e=(u,v)\in F} w_e(\phi_u + \phi_v + 2\alpha)^2\bigr]$ via the shift $\tilde\phi = \phi + \alpha\mathbf{1}_V$ (which leaves all unflipped edges invariant!). For $|F| = 1$ ($e^* = (u,v)$), $\alpha^* = -(\phi_u + \phi_v)/2$ annihilates the flipped-edge term identically, giving $\Lambda_B^{\mathrm{red}}(\chi_{e^*}) \equiv \Lambda_B^{(G\setminus\{e^*\})}(1)$; Sherman–Morrison on $L_{II} - w_{e^*} b_{e^*} b_{e^*}^\top$ yields the Rayleigh rank-1 difference $-\frac{w_{e^*}}{c_{\mathrm{harm}}^{(B)}(e^*)}(h_u - h_v)(h_u - h_v)^\top$, and Sylvester's inertia law on $+\frac{1}{\Phi_B} v v^\top - \frac{w_{e^*}}{c_{\mathrm{harm}}^{(B)}} \Delta h \Delta h^\top$ (since $v^\top \mathbf{1}_B = \Phi_B > 0$ while $\Delta h^\top \mathbf{1}_B = 0$) gives the exact trichotomy. For $|F| \ge 2$, the residual $\min_\alpha \sum_{e\in F} w_e(\phi_u+\phi_v+2\alpha)^2 \ge 0$ yields the PSD variance bound of rank $\le |F|-1$.
- **Part 4:** Deck involution commutes with $\tilde L_\sigma$ and preserves $\tilde B, \tilde I$, hence commutes with Schur elimination. For a $d$-regular Ramanujan lift, $A_\chi^2 \preceq 4(d-1)I \implies L^{(\chi)} = d I - A_\chi \succeq (d - 2\sqrt{d-1})I$, so $\Phi_B(\chi) = \min_{\phi|_B = \mathbf{1}_B} \phi^\top L^{(\chi)}\phi \ge (d - 2\sqrt{d-1})(|B| + \|\phi_I\|_2^2) \ge (d - 2\sqrt{d-1})|B|$. $\square$

---

## 3. Exact Missing-Gap Ledger (What Separates This from a Continuum "Hawking Theorem")

In strict compliance with `#263` and Aletheia Laws 4–5, **3 exact mathematical barriers** remain between this discrete finite-graph theorem and continuum quantum gravity:
1. **Continuum UV Barrier:** Positive finite graph weights $w_e \in \mathbb{Q}_{>0}$ avoid continuum Lorentzian causal singularities and UV divergences; continuum extension requires elliptic/hyperbolic Steklov-operator renormalization.
2. **Non-Abelian & Gravitational Curvature Barrier:** Flat $U(1)/\mathbb{Z}_2$ connections obey $d_1 d_0 = 0$; genuine gravitational/BMS soft-hair holonomy involves nonlinear non-Abelian diffeomorphism/Lorentz curvature ($D_A^2 = F_A \neq 0$).
3. **Dynamical Backreacting QES Barrier:** Our parallel-sum screening inequality $\le \frac{C_{\mathrm{cut}}\mathcal{E}_{\mathrm{hol}}}{C_{\mathrm{cut}}+\mathcal{E}_{\mathrm{hol}}}$ is a static variational Schur crossover between cut conductance and holonomy energy — NOT a dynamical semiclassical Einstein equation coupling $\operatorname{Area}/4G_N$ to bulk quantum entropy $S_{\mathrm{bulk}}$.

---

## 4. Reproducibility & R4/R5 Verification

From `symbiosis/round4/hawking-theorem/`:

```bash
for m in "-I -B" "-I -O -B" "-I -B -W error" "-I -O -B -W error"; do
  python3 $m boundary_double_schur_hodge_theorem.py --json | sha256sum
  python3 $m test_hawking_theorem_r5.py
done
```
