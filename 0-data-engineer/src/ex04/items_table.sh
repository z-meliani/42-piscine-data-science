#!/bin/bash
set -euo pipefail

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
