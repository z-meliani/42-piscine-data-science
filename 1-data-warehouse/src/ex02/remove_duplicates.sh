#!/bin/bash

set -euo pipefail


# Remove duplicated rows.
# Rows are duplicates of each others if they have the same column values
# and an event_time difference less or equals to a second.
psql -U $POSTGRES_USER -d $POSTGRES_DB <<'EOF'

WITH duplicates AS (
    SELECT ctid,
           LAG(event_time) OVER (
               PARTITION BY event_type,
                            product_id,
                            price,
                            user_id,
                            user_session
               ORDER BY event_time
           ) AS prev_time,
           event_time
    FROM customers
)
DELETE FROM customers c
USING duplicates d
WHERE c.ctid = d.ctid
  AND d.prev_time IS NOT NULL
  AND d.event_time - d.prev_time <= INTERVAL '1 SECOND';

EOF
