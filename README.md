# `Foundation-0/hawking`

> *"We must try to understand the universe as it really is, not as our coordinates wish it to be."*
> Dedicated in deep scientific respect to **Dr. Stephen Hawking** (1942–2018) — honoring his intellectual honesty by building **exact, zero-float, falsifiable operator instruments** and refusing to blur discrete theorems into continuum quantum-gravity claims.

`hawking` is a **zero-dependency, pure Python 3 standard-library** (`fractions.Fraction`, exact integers, and $\mathbb{Q}[i]$) verification suite investigating **coordinate-free horizon Schur complements, Krein indefinite inertia, $p$-adic BTZ holography, Čech–Hodge–Farkas observer sheaves, surgical $\mathbb{Z}_2$ edge-severing, and Ramanujan signed 2-lift spectral floors**.

- **Zero third-party dependencies** (pure Python 3 stdlib only, `>=3.10`)
- **Zero floating-point numbers** in any theorem, verification check, or JSON receipt
- **Zero bare `assert`s** (all checks remain active under `python3 -O`)
- **Bit-identical deterministic receipts** across isolated interpreter modes (`-I -B`, `-I -O -B`, `-I -B -W error`, `-I -O -B -W error`)
- **Strict Epistemic Honesty (Law 4 & Law 5):** Every classical and modern root is explicitly quarantined as `N0` prior art, and the **3 exact mathematical gaps** separating these finite discrete theorems from continuum Lorentzian quantum gravity are stated up front.

---

## Quickstart

```bash
# List all 4 exact verification modules (runs cleanly from a fresh clone; or `pip install -e .` first)
PYTHONPATH=. python3 -s -B -m hawking list

# Run the entire zero-float verification suite and print canonical SHA-256 receipts
PYTHONPATH=. python3 -s -B -m hawking verify

# Emit canonical JSON receipt bundle
PYTHONPATH=. python3 -s -B -m hawking verify --json

# Run the full isolated (-I) test suite (all 4 modules + R5 mutation-killing suites + CLI checks)
python3 -I -B tests/run_all.py
```

---

## Modules & Verified Audit Receipts

| Module | Audit | Scope | Exact Core Result (Zero Floats) | Report |
|---|---|---|---|---|
| `hawking.horizon_schur_modular` | `AUDIT-041` (`VERIFIED`, `N1`) | Singular-horizon Schur/Krein inertia, pure-$\mathbb{Q}$ Page turnaround, 4-regime modular-Schur & GKSL obstructions | Tripartite Krein null-coupling $n_- = r_{\mathrm{cross}}$ (`GL`-invariant); `N=6` pure-$\mathbb{Q}$ Page peak `R_opt(3) = 379159745830503169/224085058073528989 <= 8` (`~1.692`); Werner $\mathcal{C}_{\mathrm{GKSL}} \equiv \frac{32}{3}\mathcal{O}_{\mathrm{clock}}$ constant over all $O(2,\mathbb{Q})$ & reciprocal $\mathfrak{su}(2)$ Schur freezing $S_{\mathrm{mod}}|_{\mathfrak{su}(2)} = \lambda(q)^{-1}$; GKSL Zeno Schur rate $2g^2/\gamma = 9/50$. | [HORIZON_SCHUR_MODULAR_REPORT.md](reports/HORIZON_SCHUR_MODULAR_REPORT.md) |
| `hawking.padic_btz_leech` | `AUDIT-042` (`VERIFIED`, `N1`) | $p$-Adic Bruhat–Tits / BTZ DtN holography, $\Delta$-Y scalar blindness, $\mathbb{Z}_2$ holonomy unmasking & extremal Leech $\Lambda_{24}$ modularity | Exact vacuum $p$-adic DtN scaling; `BTZ L=3` vs `Y-star` identical scalar $\Lambda_0$ unmasked by $\mathbb{Z}_2$ holonomy rank jump $|B|-1 \to |B|$; pure-integer $Z_{\Lambda_{24}} = \Theta_{\Lambda_{24}}/\Delta$ (`q^1 = 196884 = 196560 + 324`, `691` congruence, `N0` baseline); exact valuation audit of `padic-ml`. | [PADIC_BTZ_LEECH_REPORT.md](reports/PADIC_BTZ_LEECH_REPORT.md) |
| `hawking.observer_sheaf_mdr` | `AUDIT-043` (`VERIFIED`, `N1`) | Model-Dependent Realism as exact $\mathbb{Q}$ 3-term Čech–Hodge–Farkas–Tropical duality & finite Lawvere–Gödel gate | Exact 3-term orthogonal split $\kappa_{\mathrm{grad}}+\kappa_{\mathrm{curl}}+\kappa_{\mathrm{harm}}=1$ across 3 regimes (incl. 8-triangle annular horizon ribbon with $d_1 c = 0$ yet $\kappa_{\mathrm{harm}} > 0$); Schur effective-resistance parity $c_{\mathrm{harm}}(e) = 1 - R_{\mathrm{eff}}(e)$; strict $\ell_2 > \ell_\infty$ tropical separation $15/11 > 1$; $\mathrm{Aff}^+(1,\mathbb{Q})/PGL(2,\mathbb{Q})$ equalizer tower; finite Lawvere–Gödel diagonal & acyclic dual-kernel gate. | [OBSERVER_SHEAF_MDR_REPORT.md](reports/OBSERVER_SHEAF_MDR_REPORT.md) |
| `hawking.boundary_double_schur_hodge` | `AUDIT-047` (`N2` Finite-Graph Theorem) | **Boundary Double-Schur Holographic Hodge-1, Surgical Krein-Severing, Parallel-Sum Horizon-Screening & Ramanujan 2-Lift Theorem** | Four unified universal laws over **every** finite connected positive-weighted graph $(G, w)$ and non-empty boundary $B \subseteq V$: **(1)** Double-Schur $\mathcal{H}_\partial(c) \equiv \|\Pi_{H^1} c\|_W^2$ recovering full $\beta_1(G)$ period matrix from $|\partial|=1$; **(2)** Exact finite-$(t,\varepsilon)$ parallel-sum screening $\le \frac{C_{\mathrm{cut}}\mathcal{E}_{\mathrm{hol}}}{C_{\mathrm{cut}}+\mathcal{E}_{\mathrm{hol}}}$ & non-commuting decoupling limits; **(3)** Universal **Surgical Edge-Severing Identity** $\Lambda_B^{\mathrm{red}}(\chi_{e^*}) \equiv \Lambda_B^{(G\setminus\{e^*\})}(1)$, exact 3-way Krein inertia trichotomy $(1,|B|-2,1) / (1,|B|-1,0) / (0,|B|,0)$ (with weighted-$K_4$ counterexample refuting the naive $\mathbf{1}_B^\perp$-restriction guess!), and multi-edge PSD variance bound $\Lambda_B^{\mathrm{red}}(\chi_F) \succeq \Lambda_B^{(G\setminus F)}(1)$; **(4)** Exact $\mathbb{Q}$ 2-lift deck splitting & square-root-free **Ramanujan monopole spectral floor** with 12-vertex non-Ramanujan boundary falsifier ($529/64 > 8$). | [HAWKING_THEOREM_PROGRAM.md](docs/HAWKING_THEOREM_PROGRAM.md) |

---

## Strict Law-4 `N0` Prior-Art Quarantine

Every classical and modern foundation used as a baseline or ingredient is explicitly credited in [HAWKING_PORTALS_AND_PRIOR_ART.md](docs/HAWKING_PORTALS_AND_PRIOR_ART.md) and [HAWKING_THEOREM_PROGRAM.md](docs/HAWKING_THEOREM_PROGRAM.md) and is **never** claimed as new:
- **Linear Algebra & Schur Complements:** Sylvester (1852), Schur (1917), Haynsworth (1968), Albert (1969), Benzi–Golub–Liesen (2005).
- **Electrical Networks, Hodge-1 & Signed Graphs:** Kirchhoff (1847), Kennelly (1899), Farkas (1902), Eckmann (1944), Foster (1948), Harary (1953), Zaslavsky (1982), Forman (1993), Curtis–Ingerman–Morrow (1998), Bilu–Linial (2006), Kenyon (2011), Berkolaiko–Kuchment (2013), Marcus–Spielman–Srivastava (2015), Lange–Liu–Peyerimhoff–Post (2015).
- **Black Holes, Modular Theory & $p$-Adic Holography:** Takesaki (1972), Hawking (1974, 1976, 2002, 2010), GKSL (1976), Page (1993), Connes–Rovelli (1994), Witten (2007), Gubser et al. (2016), Heydeman–Marcolli–Saberi–Stoica (2016), Hawking–Perry–Strominger (2016).

---

## Honest Scope & 3 Remaining Gaps to Continuum Quantum Gravity

We deliberately do **not** label our discrete unifying theorem "The Hawking Theorem" unless independently verified at full generality without overstatement. Three exact mathematical barriers remain between `hawking` and continuum Lorentzian quantum gravity:

1. **Continuum UV Barrier:** Finite positive graph conductances $w_e \in \mathbb{Q}_{>0}$ avoid Lorentzian causal singularities and UV divergences; continuum generalization requires elliptic/hyperbolic Steklov-operator renormalization.
2. **Non-Abelian & Gravitational Curvature Barrier:** Flat $U(1)/\mathbb{Z}_2$ connections obey $d_1 d_0 = 0$; genuine gravitational/BMS soft-hair holonomy involves nonlinear non-Abelian curvature ($D_A^2 = F_A \neq 0$).
3. **Dynamical Backreacting QES Barrier:** The parallel-sum horizon-screening inequality $\le \frac{C_{\mathrm{cut}}\mathcal{E}_{\mathrm{hol}}}{C_{\mathrm{cut}}+\mathcal{E}_{\mathrm{hol}}}$ is a static variational Schur crossover between cut conductance and holonomy energy — not a dynamical semiclassical Einstein equation coupling $\operatorname{Area}/4G_N$ to bulk quantum entropy $S_{\mathrm{bulk}}$.

---

## License

[MIT](LICENSE)
