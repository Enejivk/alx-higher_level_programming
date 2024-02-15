-- Creating a table named id_not_null
-- id will have default value of 1

CREATE TABLE
    IF NOT EXISTS id_not_null (
    id INTEGER DEFAULT 1,
    name VARCHAR(256)
    );