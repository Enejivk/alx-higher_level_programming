-- Calculating the total and the average of a row

SELECT SUM(score)/COUNT(score) 
AS average
FROM `second_table`;