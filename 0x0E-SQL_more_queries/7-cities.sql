--- Script that Create a database hbtn_0d_usa
--- It also create a table called cities
--- Creating database and table should not faile if there already exist

CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa;

USE DATABASE hbtn_0d_usa;

CREATE TABLE
    IF NOT EXISTS cities (
    id INTEGER UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INTEGER NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
    )

