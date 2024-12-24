-- Script to list all tables in the provided database
-- Save this file as task_3.sql

SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE();
