-- Create a dev database
-- This script prepares a dev database for the NeXa social networking application
CREATE DATABASE IF NOT EXISTS nexa_dev_db;
CREATE USER IF NOT EXISTS 'nexa_dev'@'localhost' IDENTIFIED BY 'nexa_dev_pwd';
GRANT ALL PRIVILEGES ON nexa_dev_db.* TO 'nexa_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'nexa_dev'@'localhost';