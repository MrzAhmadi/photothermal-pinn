# Real Data Sources

---

## 1 · Methodology — digitisation

All temperature–time curves were digitised from open-access (CC BY 4.0) journal figures with a
Python script (Pillow + NumPy), written with the assistance of Claude (Anthropic).

### Pipeline steps

1. **Paper discovery** — PubMed Central (PMC) search for articles that report full heating
   **and** cooling phases under CW laser irradiation of gold nanoparticles, with both phases in one
   figure and a CC BY licence.

2. **Figure download** — the original figure image of each article (URLs below).

3. **Axis calibration** — linear fit to the pixel positions of the major tick marks
   (fit residual < 0.04 axis units). Figure-specific notes are listed per dataset.

4. **Curve extraction** — colour mask per curve with the legend masked out; for every pixel
   column, the centroid of the curve's pixels (on steep segments, the largest contiguous run).

5. **Time origin and switching times** — time is shifted so that the laser switches on at t = 0
   (last baseline sample before the rise); `T_env` is the median of the pre-switch-on baseline;
   `t_off` is the last sample before the temperature falls 0.3 °C below its running maximum,
   unless the protocol fixes it (Dataset 1: 900 s).

6. **Resampling** — linear interpolation onto a 10 s grid, separately for the heating and the
   cooling phase. **No smoothing and no model fit are applied.**

Before 2026-09-29, the files for Datasets 1–2 stored an ODE fit to the digitised points instead
of the points themselves, and Datasets 3–4 used an axis calibration anchored on an assumed peak
(64 °C at 25 min) instead of the tick marks. All four files were rebuilt with the pipeline above;
the old versions remain in the git history.

### Error estimates

| Source | Magnitude |
|--------|-----------|
| Line centroid / pixel size | ±0.05–0.14 °C, ±2.5–6.6 s |
| Axis calibration (tick-fit residual) | < 0.04 °C, < 2 s |
| Switch-on / switch-off time | ±1 pixel column (2.5–6.6 s) |
| Single-τ ODE misfit (whole-curve fit RMS) | 0.36–1.64 °C |

---

## 2 · Datasets

The fitted `a` and `τ` below are the whole-curve least-squares fit of the single-τ ODE, used as
the reference in the notebook (`REAL_DATASETS`).

### Dataset 1 — Vikas et al. 2023

**File:** `gnr_10x38_20ugml_NIR_laser.csv` (`time_s, delta_T_C, T_C, laser_on`)
**Source figure:** [Figure 6, panel (g)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9924363/) — PMC9924363
**Image:** https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b9e7/9924363/b060c3d23503/Beilstein_J_Nanotechnol-14-205-g007.jpg

| Parameter | Value |
|-----------|-------|
| Nanoparticle | GNR 10×38 nm |
| Concentration | 20 µg/mL (green curve) |
| Laser | 808 nm CW diode laser |
| y-axis | temperature change ΔT; `T_C = 25 + ΔT` (25 °C is a nominal offset) |
| t_off | 900 s (15 min; kink of all curves in the figure) |
| Points | 179 (10–1790 s) |
| Peak ΔT | 15.5 °C |
| Fitted a / τ | 0.0456 °C/s / 381 s (t_off/τ = 2.4) |

```bibtex
@article{vikas2023,
  author  = {Vikas and Kumar, Raj and Soni, Sanjeev},
  title   = {Concentration-dependent photothermal conversion efficiency of gold nanoparticles
             under near-infrared laser and broadband irradiation},
  journal = {Beilstein Journal of Nanotechnology},
  volume  = {14},
  pages   = {205--217},
  year    = {2023},
  doi     = {10.3762/bjnano.14.20},
  note    = {Open Access, CC BY 4.0. PMCID: PMC9924363.
             Data from Figure~6(g): GNR 10x38 nm, 808 nm laser, 20 ug/mL.}
}
```

---

### Dataset 2 — Sánchez López de Pablo et al. 2014

**File:** `gnr_10x41_peg_bare_808nm_2W.csv` *(two curves; column `nanoparticle`)*
**Source figure:** [Figure 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC4155392/) — PMC4155392
**Image:** https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c84e/4155392/f5e6e60d99ac/1556-276X-9-441-6.jpg

| Parameter | B-GNR | PEG-GNR |
|-----------|-------|---------|
| Nanoparticle | GNR 10×41 nm (bare) | GNR 10×41 nm (PEG) |
| Concentration | 36 µg/mL (A_λ = 1) | 36 µg/mL (A_λ = 1) |
| Laser | 808 nm, 2.0 W CW | 808 nm, 2.0 W CW |
| Switch-on in the figure | 65.7 s (read from the PEG-GNR curve) | 65.7 s |
| t_off | 1799 s (≈ 30 min) | 1799 s |
| T_env | 25.47 °C | 25.34 °C |
| Points | 314 | 332 |
| Peak ΔT | 20.2 °C | 24.6 °C |
| Fitted a / τ | 0.0874 °C/s / 228 s (t_off/τ = 7.9) | 0.1149 °C/s / 220 s (t_off/τ = 8.2) |

The B-GNR baseline is hidden under the other curves, so its switch-on time is taken from the
PEG-GNR curve of the same figure. At the end of the record both cooling tails remain above the
initial baseline (by 1.2 °C and 2.0 °C); the water control also drifts up by about 0.6 °C.

```bibtex
@article{sanchez2014,
  author  = {S\'{a}nchez L\'{o}pez de Pablo, Cristina and
             Serrano Olmedo, Jos\'{e} Javier and
             Mina Rosales, Alejandra and
             Ram\'{i}rez Hern\'{a}ndez, Norma and
             del Pozo Guerrero, Francisco},
  title   = {A method to obtain the thermal parameters and the photothermal
             transduction efficiency in an optical hyperthermia device
             based on laser irradiation of gold nanoparticles},
  journal = {Nanoscale Research Letters},
  volume  = {9},
  number  = {1},
  pages   = {441},
  year    = {2014},
  doi     = {10.1186/1556-276X-9-441},
  note    = {Open Access, CC BY 4.0. PMCID: PMC4155392.
             Data from Figure~6: bare GNR and PEG-GNR, 10x41 nm, 808 nm, 2 W.}
}
```

---

### Dataset 3 — Armenta-Gamez et al. 2026 (AuNR)

**File:** `aunr_785nm_1p2Wcm2_pmc13028931.csv`
**Source figure:** [Figure 4A](https://pmc.ncbi.nlm.nih.gov/articles/PMC13028931/) — PMC13028931 (red curve)
**Image:** https://pub.mdpi-res.com/pharmaceutics/pharmaceutics-18-00310/article_deploy/html/images/pharmaceutics-18-00310-g004.png

| Parameter | Value |
|-----------|-------|
| Nanoparticle | AuNR (bare gold nanorods) |
| Concentration | 50 µg/mL |
| Laser | 785 nm, 1.2 W/cm² CW (spot diameter 5 mm) |
| Switch-on in the figure | 178.8 s |
| t_off | 1347 s (22.5 min by the figure's tick marks) |
| T_env | 23.85 °C |
| Points | 190 |
| Peak ΔT | 38.9 °C (T_peak = 62.8 °C) |
| Fitted a / τ | 0.1053 °C/s / 377 s (t_off/τ = 3.6) |

Figure notes: the x tick labelled "35" sits at the 30-min position (uniform tick spacing). The
article text states 25 min of irradiation and a 64 °C peak; the figure's own tick marks give
22.5 min and 62.8 °C, and the figure is used.

```bibtex
@article{armentagamez2026,
  author  = {Armenta-Gamez, Annel and Pedroza-Montero, Alejandro and
             Tapia-Villasenor, Alejandra and Silva-Campa, Erika and Loro, Hector and
             Melendrez, Rodrigo and Aguila, Sergio A. and Santacruz-Gomez, Karla},
  title   = {Gold Nanorods Embedded in Mesoporous Silica for Photothermal Therapy
             and SERS Monitoring in T47D Breast Cancer Cells},
  journal = {Pharmaceutics},
  volume  = {18},
  number  = {3},
  pages   = {310},
  year    = {2026},
  doi     = {10.3390/pharmaceutics18030310},
  note    = {Open Access, CC BY 4.0. PMCID: PMC13028931.
             Data from Figure~4A: AuNR (red) and AuNR@Si (blue), 785 nm, 1.2 W/cm2.}
}
```

---

### Dataset 4 — Armenta-Gamez et al. 2026 (AuNR@Si)

**File:** `aunrsi_785nm_1p2Wcm2_pmc13028931.csv`
**Source figure:** same as Dataset 3 (blue curve)

| Parameter | Value |
|-----------|-------|
| Nanoparticle | AuNR@Si (gold nanorods in a mesoporous silica shell) |
| Concentration | 50 µg/mL |
| Laser | 785 nm, 1.2 W/cm² CW (spot diameter 5 mm) |
| Switch-on in the figure | 196.2 s |
| t_off | 1255 s (20.9 min by the figure's tick marks) |
| T_env | 24.15 °C |
| Points | 181 |
| Peak ΔT | 20.9 °C (T_peak = 45.0 °C) |
| Fitted a / τ | 0.0928 °C/s / 221 s (t_off/τ = 5.7) |

The curve shows a fast initial rise after switch-on and a fast drop of about 4 °C within 20 s
after switch-off, followed by a slower relaxation. Citation: `armentagamez2026` above.

---

## Files in this folder

| File | Description |
|------|-------------|
| `gnr_10x38_20ugml_NIR_laser.csv` | **Dataset 1** (Vikas 2023) — 179 points, 10 s grid |
| `gnr_10x41_peg_bare_808nm_2W.csv` | **Dataset 2** (Sánchez López de Pablo 2014) — B-GNR (314) + PEG-GNR (332) |
| `aunr_785nm_1p2Wcm2_pmc13028931.csv` | **Dataset 3** (Armenta-Gamez 2026) — AuNR, 190 points |
| `aunrsi_785nm_1p2Wcm2_pmc13028931.csv` | **Dataset 4** (Armenta-Gamez 2026) — AuNR@Si, 181 points |
