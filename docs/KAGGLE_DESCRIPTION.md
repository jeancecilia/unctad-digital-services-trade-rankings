# UNCTAD Yearly Top-N Digital Services Trade Rankings

## Overview
This dataset provides easy-to-quote yearly rankings derived from UNCTAD Digital Economy and Technology data (via World Bank Data360 export).

Each year is ranked by:
- Digitally-deliverable services **exports** (USD millions)
- Digitally-deliverable services **imports** (USD millions)

The rankings are derived from the country-year panel:
- `datasets/unctad_country_year_digital_services_trade_panel.csv`

## Files
- `datasets/unctad_top20_dig_services_exports_per_year.csv`
  - Top 20 countries per year by digitally-deliverable services exports.
- `datasets/unctad_top20_dig_services_imports_per_year.csv`
  - Top 20 countries per year by digitally-deliverable services imports.

## Units
All values are in **USD millions**.

## Default scope (clean rankings)
By default, the build script excludes aggregate geographies (e.g. World) to keep the rankings country-focused.

## Output columns
### Exports ranking (`unctad_top20_dig_services_exports_per_year.csv`)
- `year`
- `rank` (1 = highest exports)
- `country`
- `iso3`
- `dig_services_exports_usd_millions`

### Imports ranking (`unctad_top20_dig_services_imports_per_year.csv`)
- `year`
- `rank` (1 = highest imports)
- `country`
- `iso3`
- `dig_services_imports_usd_millions`

## How to reproduce
From the repository root:

```bash
python scripts/build_unctad_de_panel.py
python scripts/build_unctad_de_rankings.py --top-n 20
```

To include aggregate geographies such as World (WLD):

```bash
python scripts/build_unctad_de_rankings.py --top-n 20 --include-aggregates
```

## Suggested use cases
- Media / blog-ready annual “Top N” lists
- Country benchmarking dashboards
- Quickly identifying global leaders by year
