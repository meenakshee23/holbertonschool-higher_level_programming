-- Script that creates the MySQL server user user_0d_1
-- The user should have all privileges on MySQL server
-- If the user already exists, do not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
