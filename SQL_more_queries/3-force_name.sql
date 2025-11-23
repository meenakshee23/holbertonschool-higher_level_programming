-- Script that creates the table force_name
-- id INT
-- name VARCHAR(256) cannot be NULL
-- Do not fail if the table already exists
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
