-- Script to print the full description of the table 'Books' in the provided database
-- Save this file as task_4.sql

SELECT column_name, data_type, is_nullable, column_key, column_default, extra
FROM information_schema.columns
WHERE table_schema = DATABASE()
  AND table_name = 'Books';
