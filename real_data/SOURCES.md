# Data Sources and Citations

---

## Datasets

| File | BibTeX key | Extracted from | τ (s) | peak ΔT (°C) |
|------|-----------|----------------|-------|--------------|
| `gnr_10x38_20ugml_NIR_laser.csv` | `vikas2023` | Figure 6(g), GNR 10×38 nm, NIR, 20 µg/mL | 366 | 15.2 |
| `gnr_10x41_peg_bare_808nm_2W.csv` | `sanchez2014` | Figure 6, GNR 10×41 nm, 808 nm, 2 W, 36 µg/mL; two nanoparticles: B-GNR (bare) and PEG-GNR | 365/384 | 19.7/24.4 |

---

## BibTeX

### [vikas2023]

```bibtex
@article{vikas2023,
  author    = {Vikas, R. K. and Soni, Shailendra},
  title     = {Concentration-dependent photothermal conversion efficiency
               of gold nanoparticles under near-infrared laser
               and broadband irradiation},
  journal   = {Beilstein Journal of Nanotechnology},
  volume    = {14},
  pages     = {205--217},
  year      = {2023},
  doi       = {10.3762/bjnano.14.20},
  note      = {Open Access, CC BY 4.0. PMCID: PMC9924363.
               Data digitized from Figure~6(g).}
}
```

### [sanchez2014]

```bibtex
@article{sanchez2014,
  author    = {S\'{a}nchez L\'{o}pez de Pablo, Carlos and
               Serrano Olmedo, Jos\'{e} Javier and
               Mina Rosales, Antonio and
               Ram\'{i}rez Hern\'{a}ndez, N\'{e}stor and
               del Pozo Guerrero, Francisco},
  title     = {A method to obtain the thermal parameters and the photothermal
               transduction efficiency in an optical hyperthermia device
               based on laser irradiation of gold nanoparticles},
  journal   = {Nanoscale Research Letters},
  volume    = {9},
  number    = {1},
  pages     = {441},
  year      = {2014},
  doi       = {10.1186/1556-276X-9-441},
  note      = {Open Access, CC BY 4.0. PMCID: PMC4155392.
               Data digitized from Figure~6 (B-GNR and PEG-GNR curves).}
}
```

### [wolf2023]

```bibtex
@misc{wolf2023,
  author       = {Wolf, Theo},
  title        = {Physics-Informed Neural Networks: A Simple Tutorial with PyTorch},
  year         = {2023},
  howpublished = {Medium blog post},
  url          = {https://medium.com/@theo.wolf/physics-informed-neural-networks-a-simple-tutorial-with-pytorch-f28a890b874a},
  note         = {Code: \url{https://github.com/TheodoreWolf/pinns}}
}
```

---

## Digitisation accuracy

| Source of error | Estimated magnitude |
|----------------|---------------------|
| JPEG pixel noise | ±0.3 °C in ΔT |
| Axis calibration | ±0.5 °C in ΔT, ±10 s in time |
| Analytic fit residual (RMSE) | 0.8–1.3 °C |
