-- Creating a database hbtn_0d_usa
-- Creating a table states inside the database

CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE 
IF NOT EXISTS state(
    id INT AUTO_INCREMENT NOT NULL UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);