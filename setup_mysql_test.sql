-- Create a test database
-- This script prepares a test database for the NeXa social networking application
CREATE DATABASE IF NOT EXISTS nexa_test_db;
CREATE USER IF NOT EXISTS 'nexa_test'@'localhost' IDENTIFIED BY 'nexa_test_pwd';
GRANT ALL PRIVILEGES ON nexa_test_db.* TO 'nexa_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'nexa_test'@'localhost';
