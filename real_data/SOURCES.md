# Real Data Sources

---

## 1 · Methodology — AI-assisted digitisation

All temperature–time curves were extracted from open-access (CC BY) journal figures using a
Python pipeline assisted by Claude AI (Anthropic).

### Pipeline steps

1. **Paper discovery** — Searched PubMed Central (PMC) for articles that report
   full heating **and** cooling phases under CW laser irradiation of gold nanoparticles.
   Filters: CC BY licence, both phases visible in one figure, `t_off` and `T_env` unambiguous.

2. **Figure download** — Figures downloaded from PMC Open Access CDN:
   `https://cdn.ncbi.nlm.nih.gov/pmc/blobs/{hash}/{pmcid}/{hash2}/{filename}.jpg`
   CDN URLs found via NCBI Entrez XML API (`efetch.fcgi?db=pmc&rettype=xml`).

3. **Axis calibration** — Plot area boundaries identified by scanning dark-pixel
   positions near axes. Pixel → data mapping via `np.interp` using known tick values.

4. **Curve extraction** — Colour band-pass filter on RGB values per column;
   centroid (or topmost pixel for dark-on-white curves) of matching pixels.

5. **Smoothing & resampling** — Sorted, smoothed (`uniform_filter1d`, window = N/50),
   interpolated to uniform 2–5 s resolution.

6. **Verification** — Digitised curve overlaid on original figure; ODE fit checked
   against reported τ and a values from the paper.

### Error estimates

| Source | Magnitude |
|--------|-----------|
| JPEG pixel noise | ±0.3 °C |
| Axis calibration | ±0.5 °C, ±10 s |
| Assumed T_env | ±1–2 °C |
| Analytical fit residual | 0.8–1.3 °C RMS |

---

## 2 · Datasets

### Dataset 1 — Vikas & Soni 2023

**File:** `gnr_10x38_20ugml_NIR_laser.csv`
**Source figure:** [Figure 6, panel (g)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9924363/#fig6) — PMC9924363

| Parameter | Value |
|-----------|-------|
| Nanoparticle | GNR 10×38 nm |
| Concentration | 20 µg/mL |
| Laser | NIR ~808 nm |
| t_off | 900 s |
| T_env | 25 °C (assumed) |
| t_off / τ | **2.5** ← short experiment |
| Fitted a | 0.0453 °C/s |
| Fitted τ | 366 s |
| peak ΔT | 15.2 °C |

```bibtex
@article{vikas2023,
  author  = {Vikas, R. K. and Soni, Shailendra},
  title   = {Concentration-dependent photothermal conversion efficiency
             of gold nanoparticles under near-infrared laser and broadband irradiation},
  journal = {Beilstein Journal of Nanotechnology},
  volume  = {14},
  pages   = {205--217},
  year    = {2023},
  doi     = {10.3762/bjnano.14.20},
  note    = {Open Access, CC BY 4.0. PMCID: PMC9924363.
             Data from Figure~6(g): GNR 10×38 nm, NIR, 20 µg/mL.}
}
```

---

### Dataset 2 — Sánchez et al. 2014

**File:** `gnr_10x41_peg_bare_808nm_2W.csv` *(two curves; column `nanoparticle`)*
**Source figure:** [Figure 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC4155392/#fig6) — PMC4155392

| Parameter | B-GNR | PEG-GNR |
|-----------|-------|---------|
| Nanoparticle | GNR 10×41 nm (bare) | GNR 10×41 nm (PEG) |
| Concentration | 36 µg/mL | 36 µg/mL |
| Laser | 808 nm, 2 W CW | 808 nm, 2 W CW |
| t_off | 2151 s | 2183 s |
| T_env | 26.7 °C | 26.4 °C |
| t_off / τ | **5.9** ← long experiment | **5.7** ← long |
| Fitted a | 0.0541 °C/s | 0.0636 °C/s |
| Fitted τ | 365 s | 384 s |
| peak ΔT | 19.7 °C | 24.4 °C |

```bibtex
@article{sanchez2014,
  author  = {S\'{a}nchez L\'{o}pez de Pablo, Carlos and
             Serrano Olmedo, Jos\'{e} Javier and
             Mina Rosales, Antonio and
             Ram\'{i}rez Hern\'{a}ndez, N\'{e}stor and
             del Pozo Guerrero, Francisco},
  title   = {A method to obtain the thermal parameters and the photothermal
             transduction efficiency in an optical hyperthermia device
             based on laser irradiation of gold nanoparticles},
  journal = {Nanoscale Research Letters},
  volume  = {9},
  pages   = {441},
  year    = {2014},
  doi     = {10.1186/1556-276X-9-441},
  note    = {Open Access, CC BY 4.0. PMCID: PMC4155392.
             Data from Figure~6: bare GNR and PEG-GNR, 10×41 nm, 808 nm, 2 W.}
}
```

---

### Dataset 3 — Gallo et al. 2025

**File:** `aunr_785nm_1p2Wcm2_pmc13028931.csv`
**Source figure:** [Figure 4A](https://pmc.ncbi.nlm.nih.gov/articles/PMC13028931/#fig4) — PMC13028931

| Parameter | Value |
|-----------|-------|
| Nanoparticle | AuNR (bare gold nanorods) |
| Laser | 785 nm, 1.2 W/cm² CW |
| t_off | 1520 s (~25 min) |
| T_env | 24.0 °C |
| Fitted τ | ~495 s |
| t_off / τ | **~3.1** ← medium experiment |
| peak ΔT | 40.0 °C (T_peak = 64.0 °C) |
| T at end of cooling | 33.1 °C (at t ≈ 2230 s; not fully returned to T_env) |
| Note | Red curve; same figure has Water (black) and AuNR@Si (blue, Dataset 4) |

```bibtex
@article{gallo2025,
  author  = {Gallo, Elisabetta and others},
  title   = {Gold Nanorods Embedded in Mesoporous Silica for Photothermal Therapy
             and SERS Monitoring in T47D Breast Cancer Cells},
  journal = {Pharmaceutics},
  volume  = {18},
  pages   = {310},
  year    = {2025},
  doi     = {10.3390/pharmaceutics18030310},
  note    = {Open Access, CC BY 4.0. PMCID: PMC13028931.
             Data from Figure~4A: AuNR (red) curve, 785 nm, 1.2 W/cm².}
}
```

---

### Dataset 4 — Gallo et al. 2025 (AuNR@Si)

**File:** `aunrsi_785nm_1p2Wcm2_pmc13028931.csv`
**Source figure:** [Figure 4A](https://pmc.ncbi.nlm.nih.gov/articles/PMC13028931/#fig4) — PMC13028931 *(same figure as Dataset 3, blue curve)*

| Parameter | Value |
|-----------|-------|
| Nanoparticle | AuNR@Si (gold nanorods in mesoporous silica shell) |
| Laser | 785 nm, 1.2 W/cm² CW |
| t_off | 1430 s (~24 min) |
| T_env | 24.5 °C |
| Fitted τ | ~369 s |
| t_off / τ | **~3.9** ← medium-long experiment |
| peak ΔT | 21.4 °C (T_peak = 45.9 °C) |
| T at end of cooling | 27.5 °C (at t ≈ 2150 s; nearly complete cooling) |
| Note | Blue curve from same Fig 4A panel; silica shell attenuates heating |

```bibtex
@article{gallo2025aunrsi,
  author  = {Gallo, Elisabetta and others},
  title   = {Gold Nanorods Embedded in Mesoporous Silica for Photothermal Therapy
             and SERS Monitoring in T47D Breast Cancer Cells},
  journal = {Pharmaceutics},
  volume  = {18},
  pages   = {310},
  year    = {2025},
  doi     = {10.3390/pharmaceutics18030310},
  note    = {Open Access, CC BY 4.0. PMCID: PMC13028931.
             Data from Figure~4A: AuNR@Si (blue) curve, 785 nm, 1.2 W/cm².}
}
```

---

## Files in this folder

| File | Description |
|------|-------------|
| `gnr_10x38_20ugml_NIR_laser.csv` | **Dataset 1** (Vikas 2023) — 901 pts, 2 s res. |
| `gnr_10x38_20ugml_raw_digitized.csv` | Dataset 1 raw pixels (before ODE fit) |
| `gnr_10x38_all_conc_NIR_laser.csv` | Dataset 1 all concentrations (raw) |
| `gnr_10x41_peg_bare_808nm_2W.csv` | **Dataset 2** (Sánchez 2014) — B-GNR + PEG-GNR |
| `aunr_785nm_1p2Wcm2_pmc13028931.csv` | **Dataset 3** (Gallo 2025) — AuNR red curve, 785 nm |
| `aunrsi_785nm_1p2Wcm2_pmc13028931.csv` | **Dataset 4** (Gallo 2025) — AuNR@Si blue curve, 785 nm |
