CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL,
    short_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    role TEXT,
    nationality TEXT,
    date_of_birth TEXT,
    batting_style TEXT,
    bowling_style TEXT,
    team_id INTEGER,

    FOREIGN KEY (team_id)
        REFERENCES teams(team_id)
);