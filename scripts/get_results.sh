#!/bin/bash
cat scripts/query.sql | docker exec -i etl_db psql -U postgres -d postgres