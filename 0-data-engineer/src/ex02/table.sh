#!/bin/bash
set -euo pipefail


# Create my first table using a CSV
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<EOF

DROP TABLE IF EXISTS data_2022_oct;

CREATE TABLE data_2022_oct (
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    product_id INT,
    price NUMERIC(10,2),
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_oct
FROM '/data/customer/data_2022_oct.csv'
CSV HEADER;

EOF