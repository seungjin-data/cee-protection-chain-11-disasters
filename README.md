# Repository-ready research package

## Study
Operational conversion of hazard information into human protective action across 11 major disasters

This package contains the coded analytical data and reproducibility materials prepared for a Communications Earth & Environment research article. It is designed for deposit in a public research repository (for example, Zenodo or Figshare). The archival DOI should be inserted into the manuscript only after the repository deposit is created.

## Contents

### data/
- `01_mobilisation_matrix.csv` — locality-specific institutional mobilisation decomposition. Authority, request, dispatch, arrival, deployment and field action are retained as separate operational states.
- `02_human_protection_audit.csv` — event/sub-unit adjudication of actual human action and strict pre-impact exposure evidence, including publication-facing evidential restrictions.
- `03_ahr_evidence_matrix.csv` — complete 82-row Ahr evidence matrix using the frozen 14-field schema.
- `04_protection_chain_matrix.csv` — event-level S1-S5 conversion matrix underlying Fig. 1 and Table 1, with publication-facing provenance labels.
- `05_source_registry.csv` — 185-row source registry linking the principal analytical elements across all 11 events to recorded source sets.
- `Table1_FINAL.csv`, `Table1_FINAL_condensed.csv`, `Table2_FINAL.csv`, `SupplementaryTable1_FINAL.csv`, `SupplementaryTable2_FINAL.csv` — reader-facing display derivatives.

### code/
- `fig1_render_production_helvetica.py` — publication-facing figure-generation script. It reads `data/04_protection_chain_matrix.csv`; the analytical data, coordinates, layout, colours and marker assignments are unchanged from the locked figure. The PDF uses the standard Helvetica/Helvetica-Bold PDF core fonts.

### figure/
- `Fig1_FINAL.pdf` — vector production figure using Helvetica/Helvetica-Bold.
- `Fig1_FINAL.svg` — vector SVG with Helvetica/Arial/sans-serif font family declaration.
- `Fig1_FINAL_600dpi.png` — 600 dpi raster generated from the Helvetica PDF.

### docs/
- `DATA_AVAILABILITY_DRAFT.txt`
- `CODE_AVAILABILITY_DRAFT.txt`
- `RELATED_MANUSCRIPT_OVERLAP_AUDIT.md`
- `FIG1_PRODUCTION_FONT_QC.md`

## Evidence and uncertainty rules

The public data preserve the distinction between observed evidence, documented non-execution and unresolved evidence. Missing documentation is not coded as failure. Execution state is separate from evidence status. Local impact timing is retained where event-wide timing would distort sequencing. Casualties are not used to infer protective action or exposure reduction.

Publication-facing provenance labels describe source-verification status rather than the identity of any research-support tool.

## Computational environments

- Python 3.12.3 with Matplotlib 3.10.8: analytical data processing, consistency and package-lineage checks, and original figure generation.
- Python 3.13.5 with Matplotlib 3.10.8: final production re-rendering of Fig. 1 using Helvetica fonts only.

The production re-render did not alter analytical data, classifications, coordinates, colours, markers or substantive figure content. The verification record is in `docs/FIG1_PRODUCTION_FONT_QC.md`.

## Reuse and verification

Use `CHECKSUMS_SHA256.txt` to verify package integrity. The repository DOI remains to be added by the depositing author before the deposit is finalized.

## Licence

The data files in `data/` and the documentation in `docs/` are released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). The code in `code/` is released under the MIT licence. See `LICENSE-CC-BY-4.0.txt` and `LICENSE-MIT.txt`.

## How to cite

Cite both the associated article and this archived dataset. Machine-readable citation metadata is in `CITATION.cff`.
