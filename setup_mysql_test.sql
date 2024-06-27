-- Creates a MYSQL Database hbnb_test_db
-- A new user hbnb_test in localhost
-- hbnb_trest should have all privileges on the db hbnb_test_db
-- hbnb_test should have SELECT privilege on the db performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
    ON `hbnb_test_db`.*
    TO 'hbnb_test'@'localhost';
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;