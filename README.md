# Top 20 Digital Services Trade Rankings (2010–2023 / 2025 Edition)

## Overview
This dataset provides cleaned and structured yearly rankings of **Top 20 countries by digitally-deliverable services exports and imports (USD millions)**, derived from official source data published by **UN Trade and Development (UNCTAD)**.

The dataset was created to support research, policy analysis, journalism, and data-driven content that requires **consistent country naming, comparable time series, and ready-to-use rankings**.

**Canonical dataset page:**  
https://devstackph.com/top-20-countries-by-digital-services-exports-imports-unctad-yearly-rankings/

---

## Source Data
Primary source:
- **UN Trade and Development (UNCTAD)** – *International trade in digitally deliverable services (UNCTADstat)*  
  Original publication:
  - https://unctadstat.unctad.org/datacentre/reportInfo/US.DigitallyDeliverableServices
  - https://unctadstat.unctad.org/datacentre/dataviewer/US.DigitallyDeliverableServices

The original source data was accessed on **2025-12-18**.

---

## Data Processing & Methodology
The following transformations were applied:

1. Built a clean country-year panel in **USD millions** from the UNCTAD export.
2. Excluded aggregate geographies by default to ensure country-only rankings.
3. For each year, sorted countries by value (descending) and assigned `rank`.
4. Kept the Top 20 per year for exports and imports.
5. Validated rankings against recomputed results from the underlying panel.

No imputation was performed.

---

## Dataset Contents
Files included:

- `datasets/unctad_top20_dig_services_exports_per_year.csv` – Top 20 exports per year
- `datasets/unctad_top20_dig_services_imports_per_year.csv` – Top 20 imports per year
- `docs/COLUMN_DICTIONARY.md` – Column descriptions and units
- `docs/KAGGLE_DESCRIPTION.md` – Detailed derivation notes

Key fields include:
- `year`
- `rank`
- `country`
- `iso3`
- `dig_services_exports_usd_millions` (exports file)
- `dig_services_imports_usd_millions` (imports file)

---

## Intended Use
This dataset is suitable for:
- Academic research and citation
- Policy and trade analysis
- Journalism and reporting
- SEO and content marketing with verifiable data
- Comparative country and regional studies

---

## How to Cite
If you use this dataset, please cite:

> DevStackPH (2025). *Top 20 Digital Services Trade Rankings (2010–2023 / 2025 Edition).* GitHub repository: https://github.com/jeancecilia/unctad-digital-services-trade-rankings (accessed YYYY-MM-DD).

DOI: (not yet assigned)

---

## License
This dataset is published under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

You are free to share and adapt the data, provided proper attribution is given.

---

## Related Resources
- Canonical dataset page: https://devstackph.com/top-20-countries-by-digital-services-exports-imports-unctad-yearly-rankings/
- Base panel dataset: https://devstackph.com/unctad-digital-services-trade-panel/
- Regional aggregates: https://devstackph.com/regional-digital-services-trade-aggregates-asean-eu27-g7-unctad-derived/

---

## Reproduce
```bash
python scripts/build_unctad_de_panel.py
python scripts/build_unctad_de_rankings.py --top-n 20
```

---

## Disclaimer
This dataset is a derived work. The authors are not responsible for interpretations or conclusions drawn from the data.
