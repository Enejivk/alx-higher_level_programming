-- Create a database if it doesn't already exist
-- Grant SELECT privileges on all tables 
-- in the hbtn_0d_2 database to the user

CREATE DATABASE 
    IF NOT EXISTS hbtn_0d_2;

CREATE USER
    'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT
    ON hbtn_0d_2.*
    TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;