-- Creat a user user_0d_1.
-- If the user does not exist you code should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL
ON *.*
TO 'user_0d_1_pwd'@'localhost';
IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;