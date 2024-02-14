-- list all the names except the ones that is NULL

SELECT `score`, `name` 
FROM `second_table`
WHERE name IS NOT NULL
ORDER BY `score` DESC;

