"""Build yearly top-N ranking datasets from the UNCTAD digital services trade panel."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASETS_DIR = PROJECT_ROOT / "datasets"
PANEL_FILE = DATASETS_DIR / "unctad_country_year_digital_services_trade_panel.csv"

EXPORTS_COLUMN = "dig_services_exports_usd_millions"
IMPORTS_COLUMN = "dig_services_imports_usd_millions"

AGGREGATE_ISO3_CODES: set[str] = {"WLD", "SSF"}
AGGREGATE_COUNTRY_LABELS: set[str] = {"World", "Sub-Saharan Africa"}


def filter_countries_only(df: pd.DataFrame) -> pd.DataFrame:
    """Filter out aggregate geographies (keep countries only)."""
    required_columns = {"iso3", "country"}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise KeyError(f"Missing required columns: {sorted(missing_columns)}")

    filtered = df.copy()
    filtered = filtered[~filtered["iso3"].isin(AGGREGATE_ISO3_CODES)]
    filtered = filtered[~filtered["country"].isin(AGGREGATE_COUNTRY_LABELS)]
    return filtered


def _build_yearly_ranking(
    df: pd.DataFrame,
    value_column: str,
    top_n: int,
) -> pd.DataFrame:
    required_columns = {"country", "iso3", "year", value_column}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise KeyError(f"Missing required columns: {sorted(missing_columns)}")

    ranking = df[["year", "country", "iso3", value_column]].copy()
    ranking[value_column] = pd.to_numeric(ranking[value_column], errors="coerce")
    ranking = ranking.dropna(subset=["year", value_column])

    ranking = ranking.sort_values(
        ["year", value_column, "iso3"],
        ascending=[True, False, True],
    )

    ranking["rank"] = ranking.groupby("year", sort=False).cumcount() + 1
    ranking = ranking[ranking["rank"] <= top_n]

    ranking = ranking[["year", "rank", "country", "iso3", value_column]]
    ranking["year"] = pd.to_numeric(ranking["year"], errors="coerce").astype("Int64")
    ranking["rank"] = pd.to_numeric(ranking["rank"], errors="coerce").astype(int)
    return ranking.reset_index(drop=True)


def load_panel(path: Path) -> pd.DataFrame:
    """Load the pre-built country-year panel dataset."""
    if not path.exists():
        raise FileNotFoundError(
            f"Panel file not found at {path}. Run scripts/build_unctad_de_panel.py first."
        )
    return pd.read_csv(path)


def main() -> None:
    """Entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--top-n",
        type=int,
        default=20,
        help="Number of top countries to keep per year (default: 20).",
    )
    parser.add_argument(
        "--include-aggregates",
        action="store_true",
        help="Include aggregate geographies such as World (WLD) in rankings.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    panel = load_panel(PANEL_FILE)
    if not args.include_aggregates:
        panel = filter_countries_only(panel)

    exports_ranking = _build_yearly_ranking(panel, EXPORTS_COLUMN, args.top_n)
    imports_ranking = _build_yearly_ranking(panel, IMPORTS_COLUMN, args.top_n)

    exports_file = DATASETS_DIR / f"unctad_top{args.top_n}_dig_services_exports_per_year.csv"
    imports_file = DATASETS_DIR / f"unctad_top{args.top_n}_dig_services_imports_per_year.csv"

    exports_ranking.to_csv(exports_file, index=False)
    imports_ranking.to_csv(imports_file, index=False)

    logging.info("Wrote exports ranking to %s (%s rows)", exports_file, len(exports_ranking))
    logging.info("Wrote imports ranking to %s (%s rows)", imports_file, len(imports_ranking))


if __name__ == "__main__":
    main()
