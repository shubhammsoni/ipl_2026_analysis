# ============================================================
# IPL DATA CLEANING
# ------------------------------------------------------------
# Purpose:
# Convert historical / alternate / inconsistent source names
# into consistent canonical names for analytics.
#
# IMPORTANT:
# This does NOT modify the original Cricsheet JSON files.
# ============================================================


# ============================================================
# TEAM NAME MAPPING
# ============================================================

TEAM_NAME_MAPPING = {

    # Delhi franchise
    "Delhi Daredevils": "Delhi Capitals",
    "Delhi Capitals": "Delhi Capitals",

    # Punjab franchise
    "Kings XI Punjab": "Punjab Kings",
    "Punjab Kings": "Punjab Kings",

    # Royal Challengers franchise
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
    "Royal Challengers Bengaluru": "Royal Challengers Bengaluru",

    # Historical Pune naming variation
    "Rising Pune Supergiants": "Rising Pune Supergiant",
    "Rising Pune Supergiant": "Rising Pune Supergiant",
}


def clean_team_name(team_name):
    """
    Return the canonical team/franchise name.

    If no mapping exists, retain the original name.
    """

    if team_name is None:
        return None

    team_name = team_name.strip()

    return TEAM_NAME_MAPPING.get(team_name, team_name)


# ============================================================
# VENUE NAME MAPPING
# ============================================================

VENUE_NAME_MAPPING = {

    # Bengaluru
    "M Chinnaswamy Stadium, Bengaluru":
        "M Chinnaswamy Stadium",

    "M.Chinnaswamy Stadium":
        "M Chinnaswamy Stadium",

    # Mumbai
    "Wankhede Stadium, Mumbai":
        "Wankhede Stadium",

    "Brabourne Stadium, Mumbai":
        "Brabourne Stadium",

    "Dr DY Patil Sports Academy, Mumbai":
        "Dr DY Patil Sports Academy",

    # Delhi
    "Arun Jaitley Stadium, Delhi":
        "Arun Jaitley Stadium",

    # Kolkata
    "Eden Gardens, Kolkata":
        "Eden Gardens",

    # Dharamsala
    "Himachal Pradesh Cricket Association Stadium, Dharamsala":
        "Himachal Pradesh Cricket Association Stadium",

    # Visakhapatnam
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam":
        "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",

    # Chennai
    "MA Chidambaram Stadium, Chepauk":
        "MA Chidambaram Stadium",

    "MA Chidambaram Stadium, Chepauk, Chennai":
        "MA Chidambaram Stadium",

    # Pune
    "Maharashtra Cricket Association Stadium, Pune":
        "Maharashtra Cricket Association Stadium",

    # Jaipur
    "Sawai Mansingh Stadium, Jaipur":
        "Sawai Mansingh Stadium",

    # Raipur
    "Shaheed Veer Narayan Singh International Stadium, Raipur":
        "Shaheed Veer Narayan Singh International Stadium",

    # Hyderabad
    "Rajiv Gandhi International Stadium, Uppal":
        "Rajiv Gandhi International Stadium",

    "Rajiv Gandhi International Stadium, Uppal, Hyderabad":
        "Rajiv Gandhi International Stadium",

    # Mohali / Chandigarh
    "Punjab Cricket Association IS Bindra Stadium, Mohali":
        "Punjab Cricket Association IS Bindra Stadium",

    "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh":
        "Punjab Cricket Association IS Bindra Stadium",

    # New Chandigarh / Mullanpur
    "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh":
        "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
}


def clean_venue_name(venue_name):
    """
    Return the standardized venue name.

    If the venue does not require cleaning,
    retain the original name.
    """

    if venue_name is None:
        return None

    venue_name = venue_name.strip()

    return VENUE_NAME_MAPPING.get(
        venue_name,
        venue_name
    )


# ============================================================
# CITY MAPPING
# ============================================================

CITY_NAME_MAPPING = {

    # Historical/current city naming
    "Bangalore": "Bengaluru",

    # Mullanpur venue
    "Mohali": "New Chandigarh",
}


def clean_city_name(city):
    """
    Standardize known city-name variations.
    """

    if city is None:
        return None

    city = city.strip()

    return CITY_NAME_MAPPING.get(city, city)


# ============================================================
# VENUE-SPECIFIC CITY CORRECTIONS
# ============================================================

VENUE_CITY_MAPPING = {

    "M Chinnaswamy Stadium":
        "Bengaluru",

    "Dubai International Cricket Stadium":
        "Dubai",

    "Sharjah Cricket Stadium":
        "Sharjah",

    "Dr DY Patil Sports Academy":
        "Navi Mumbai",

    "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur":
        "New Chandigarh",
}


def clean_venue_city(venue_name, city):
    """
    Standardize a venue and its city together.

    Venue-specific city mappings take priority because
    some source JSON files contain missing or inconsistent
    city values.
    """

    clean_venue = clean_venue_name(venue_name)

    if clean_venue in VENUE_CITY_MAPPING:
        clean_city = VENUE_CITY_MAPPING[clean_venue]
    else:
        clean_city = clean_city_name(city)

    return clean_venue, clean_city