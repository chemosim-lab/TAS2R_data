# TAS2R_data

Code and data for the TAS2R paper:
```
Placeholder for the article's reference...
```

## Description
---

- `mammalian-TAS2R.pir`: MSA of mammalian TAS2R sequences
- `TAS2R-OR-templates.pir`: MSA used to generate the homology models
- `TAS2R-msa-annotated.xlsx`: Excel spreadsheet containing the annotated sequence
- The `3D models` directory contains the PDB files for each of the 25 human TAS2R models
with the highest meta-score. The tempfactor inside the PDB file has been modified to
correspond to the sequence identity between TAS2Rs.
- The `scripts` directory contains the code that was used in the current paper:
  - `01-generate-models.py`: Modeller script used to generate 3D models of TAS2Rs
  - `02-analysis.ipynb`: Analysis notebook to score all models
  - `pocket.pdb`: Set of points used to generate the binding pocket of the receptor used for scoring
  - `msa.xlsx`: Simplified version of the `TAS2R-msa-annotated.xlsx` file
  - `all_scores_models_final.pkl`: The complete table of scores for each receptor and protocol (without missfolded models)

## Requirements
---

```
mdanalysis=1.0.0
modeller=9.21
numpy=1.19.0
pandas=1.0.1
scipy=1.5.0
```