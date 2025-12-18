# UNCTAD Digital Services Trade Rankings

Yearly Top-20 country rankings derived from UNCTAD digitally-deliverable services trade (USD millions).

## Datasets
- datasets/unctad_top20_dig_services_exports_per_year.csv
- datasets/unctad_top20_dig_services_imports_per_year.csv

## Backlinks
- WordPress post: https://devstackph.com/top-20-countries-by-digital-services-exports-imports-unctad-yearly-rankings/

## How to cite
If you use this dataset, please cite it as:

> Cecilia Menzel, Jean Maurice. (2025). Top 20 Countries by Digital Services Exports & Imports (UNCTAD, Yearly Rankings). GitHub repository: https://github.com/jeancecilia/unctad-digital-services-trade-rankings (accessed YYYY-MM-DD).

## Reproduce
```bash
python scripts/build_unctad_de_panel.py
python scripts/build_unctad_de_rankings.py --top-n 20
```

See docs/KAGGLE_DESCRIPTION.md for the full dataset description.
