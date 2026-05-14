#!/bin/bash

set -euo pipefail


# Join the customers and the items table
psql -U $POSTGRES_USER -d $POSTGRES_DB <<'EOF'

DROP TABLE IF EXISTS customers_new;

CREATE TABLE customers_new AS
WITH items_agg AS (
    SELECT
        product_id,

        jsonb_agg(DISTINCT category_id)
            FILTER (WHERE category_id IS NOT NULL) AS category_id,

        jsonb_agg(DISTINCT category_code)
            FILTER (WHERE category_code IS NOT NULL) AS category_code,

        jsonb_agg(DISTINCT brand)
            FILTER (WHERE brand IS NOT NULL) AS brand

    FROM items
    GROUP BY product_id
)

SELECT c.*, ia.category_id, ia.category_code, ia.brand
FROM customers c
LEFT JOIN items_agg ia
    ON c.product_id = ia.product_id;

BEGIN;

DROP TABLE customers;
ALTER TABLE customers_new RENAME TO customers;

COMMIT;

DROP TABLE items;

EOF
