#!/bin/bash
set -euo pipefail


# Create a template table for columns and data types
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<EOF

DROP TABLE IF EXISTS template_customer;

CREATE TABLE template_customer (
    event_time TIMESTAMP,
    user_id BIGINT,
    user_session UUID,
    event_type VARCHAR(50),
    product_id INT,
    price NUMERIC(10,2)
);

EOF


# Create tables with data from CSV files and template_customer table structure
for file in /data/customer/*.csv; do

  table=$(basename "$file" .csv | tr -cd 'a-zA-Z0-9_')

  echo "Creating table: $table"

  psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<EOF

DROP TABLE IF EXISTS "$table";

CREATE TABLE "$table" (LIKE template_customer INCLUDING ALL);

COPY "$table" (event_time, event_type, product_id, price, user_id, user_session)
FROM '$file'
CSV HEADER;

EOF
done

# Delete template_customer table
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<EOF
DROP TABLE IF EXISTS template_customer;
EOF


# Create tables with data from CSV files and template_customer table structure
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<EOF

DROP TABLE IF EXISTS items;

CREATE TABLE items (
    product_id INT,
    category_id BIGINT,
    category_code TEXT,
    brand VARCHAR(50)
);

COPY items (product_id, category_id, category_code, brand)
FROM '/data/item/item.csv'
CSV HEADER;

EOF
