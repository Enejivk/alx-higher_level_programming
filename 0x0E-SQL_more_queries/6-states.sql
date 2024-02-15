-- Creating a database hbtn_0d_usa
-- Creating a table states inside the database

CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE
    IF NOT EXISTS states (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(256),
    UNIQUE(id)
    );
