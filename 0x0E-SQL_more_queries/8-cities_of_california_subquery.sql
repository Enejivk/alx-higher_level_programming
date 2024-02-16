-- Printing The list of all the cities in California
-- In ascending order

SELECT id, name
    FROM cities
    WHERE state_id = 1
    ORDER BY id ASC;

