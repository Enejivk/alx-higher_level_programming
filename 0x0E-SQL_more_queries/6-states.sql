-- Creating a database hbtn_0d_usa
-- Creating a table states inside the database

CREATE database 
    IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;
CREATE table I
    F NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL);