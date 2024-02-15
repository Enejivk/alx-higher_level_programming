-- Creating a Database Table name force_name

CREATE TABLE 
    IF NOT EXISTS force_name(
    force_name TEXT,
    id INTEGER,
    name VARCHAR(256) NOT NULL
    );
