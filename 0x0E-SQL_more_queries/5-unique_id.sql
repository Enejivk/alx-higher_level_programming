-- Creating a table unique_id
-- Giving it a unique id

CREATE TABLE
    IF NOT EXISTS unique_id (
    id INTEGER DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
    );