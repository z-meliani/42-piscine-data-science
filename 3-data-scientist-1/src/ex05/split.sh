#!/bin/bash

TRAIN_FILE="Training_knight.csv"
VAL_FILE="Validation_knight.csv"
FILE_PATH="$1"
FILENAME=$(basename "$FILE_PATH")

# Check if a file argument was provided
if [ -z "$FILE_PATH" ]; then
    echo "Usage: $0 <filename.csv>"
    exit 1
fi

# Check if the file actually exists
if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File '$FILE_PATH' not found."
    exit 1
fi

# Extract the header and count total lines (excluding header)
HEADER=$(head -n 1 "$FILE_PATH")
TOTAL_LINES=$(wc -l < "$FILE_PATH")
DATA_LINES=$((TOTAL_LINES - 1))

if [ "$DATA_LINES" -le 0 ]; then
    echo "Error: The CSV file does not contain data."
    exit 1
fi

# Calculate line counts for 80% split (Validation gets the remainder)
TRAIN_COUNT=$(( (DATA_LINES * 80) / 100 ))
VAL_COUNT=$(( DATA_LINES - TRAIN_COUNT ))

echo "$FILENAME : $DATA_LINES rows"
echo "$TRAIN_FILE : $TRAIN_COUNT rows"
echo "$VAL_FILE : $VAL_COUNT rows"

# Initialize output files with the header row
echo "$HEADER" > Training_knight.csv
echo "$HEADER" > Validation_knight.csv


# 1. 'tail' skips the header
# 2. 'shuf' randomly shuffles all data rows
# 3. 'head' and 'tail' split the shuffled stream into the respective files
tail -n +2 "$FILE_PATH" | shuf | {
    head -n "$TRAIN_COUNT" >> Training_knight.csv;
    tail -n "$VAL_COUNT" >> Validation_knight.csv;
}