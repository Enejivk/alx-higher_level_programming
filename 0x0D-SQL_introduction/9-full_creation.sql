-- Creating a full table with values

CREATE TABLE IF NOT EXISTS `testing2`(
    id INT,
    name VARCHAR(256),
    score INT
    );

INSERT INTO `testing2` (id, name, score) 
VALUES 
    ('1', 'John', '10'),
    ('2', 'Alex', '3'),
    ('3', 'Bob', '14'),
    ('4', 'George', '8');
