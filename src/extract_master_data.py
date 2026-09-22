import json
from pathlib import Path

from src.data_cleaning import (
    clean_team_name,
    clean_venue_city
)


# ============================================================
# CONFIGURATION
# ============================================================

json_folder = Path("data/raw/ipl_json")


# ============================================================
# RAW DATA COLLECTION
# ============================================================

raw_teams = set()
raw_venues = set()


# ============================================================
# CLEAN DATA COLLECTION
# ============================================================

clean_teams = set()
clean_venues = set()


# ============================================================
# FIND JSON FILES
# ============================================================

json_files = list(json_folder.glob("*.json"))

print(f"JSON files found: {len(json_files)}")


# ============================================================
# PROCESS EVERY MATCH
# ============================================================

for file_path in json_files:

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    info = data["info"]


    # --------------------------------------------------------
    # TEAMS
    # --------------------------------------------------------

    for team in info.get("teams", []):

        raw_teams.add(team)

        cleaned_team = clean_team_name(team)

        clean_teams.add(cleaned_team)


    # --------------------------------------------------------
    # VENUES
    # --------------------------------------------------------

    venue = info.get("venue")
    city = info.get("city")

    if venue:

        raw_venues.add(
            (venue, city)
        )

        cleaned_venue, cleaned_city = clean_venue_city(
            venue,
            city
        )

        clean_venues.add(
            (cleaned_venue, cleaned_city)
        )


# ============================================================
# RAW TEAMS
# ============================================================

print("\n")
print("=" * 70)
print("RAW TEAMS")
print("=" * 70)

for team in sorted(raw_teams):
    print(team)


# ============================================================
# CLEAN TEAMS
# ============================================================

print("\n")
print("=" * 70)
print("CLEAN / CANONICAL TEAMS")
print("=" * 70)

for team in sorted(clean_teams):
    print(team)


# ============================================================
# RAW VENUES
# ============================================================

print("\n")
print("=" * 70)
print("RAW VENUES")
print("=" * 70)

for venue, city in sorted(
    raw_venues,
    key=lambda x: (x[0] or "", x[1] or "")
):
    print(f"{venue} | {city}")


# ============================================================
# CLEAN VENUES
# ============================================================

print("\n")
print("=" * 70)
print("CLEAN / CANONICAL VENUES")
print("=" * 70)

for venue, city in sorted(
    clean_venues,
    key=lambda x: (x[0] or "", x[1] or "")
):
    print(f"{venue} | {city}")


# ============================================================
# DATA QUALITY CHECK
# ============================================================

missing_city_venues = [
    (venue, city)
    for venue, city in clean_venues
    if city is None
]


# ============================================================
# SUMMARY
# ============================================================

print("\n")
print("=" * 70)
print("CLEANING SUMMARY")
print("=" * 70)

print(f"JSON files processed : {len(json_files)}")

print()
print("TEAMS")
print(f"Raw team names       : {len(raw_teams)}")
print(f"Canonical teams      : {len(clean_teams)}")
print(f"Names consolidated   : {len(raw_teams) - len(clean_teams)}")

print()
print("VENUES")
print(f"Raw venue records    : {len(raw_venues)}")
print(f"Canonical venues     : {len(clean_venues)}")
print(f"Records consolidated : {len(raw_venues) - len(clean_venues)}")

print()
print("DATA QUALITY")
print(f"Missing cities       : {len(missing_city_venues)}")


if missing_city_venues:

    print("\nStill missing city:")

    for venue, city in sorted(
        missing_city_venues,
        key=lambda x: x[0] or ""
    ):
        print(f"{venue} | {city}")