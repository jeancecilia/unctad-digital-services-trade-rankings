# UNCTAD Digital Services Trade Rankings

Yearly Top-20 country rankings derived from UNCTAD digitally-deliverable services trade (USD millions).

## Datasets
- datasets/unctad_top20_dig_services_exports_per_year.csv
- datasets/unctad_top20_dig_services_imports_per_year.csv

## Reproduce
`ash
python scripts/build_unctad_de_panel.py
python scripts/build_unctad_de_rankings.py --top-n 20
`

See docs/KAGGLE_DESCRIPTION.md for the full dataset description.
