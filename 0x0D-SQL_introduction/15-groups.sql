-- Returning the list of all duplicated value

SELECT `score`, COUNT(score) As number
FROM `second_table`
GROUP BY score
ORDER BY `score` DESC;