#!/bin/bash

set -euo pipefail


# Join tables with names as 'data_20**_***'
psql -U $POSTGRES_USER -d $POSTGRES_DB <<'EOF'

DROP TABLE IF EXISTS customers;

-- Create customers table
DO $$
DECLARE
    sql text;
BEGIN
    SELECT 'CREATE TABLE customers AS ' ||
           string_agg(format('SELECT * FROM %I', tablename), ' UNION ')
    INTO sql
    FROM pg_tables
    WHERE schemaname = 'public'
      AND tablename ~ '^data_[0-9]{4}_(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)$';

    EXECUTE sql;
END $$;

-- Drop 'data_20**_**' tables
DO $$
DECLARE
    r record;
BEGIN
    FOR r IN
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = 'public'
          AND tablename ~ '^data_[0-9]{4}_(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)$'
    LOOP
        EXECUTE format('DROP TABLE IF EXISTS %I CASCADE', r.tablename);
    END LOOP;
END $$;

EOF
