#!/bin/bash

# Script to update BUILD timestamp in hyperexecute.yaml
# Usage: ./update_build_timestamp.sh

set -e  # Exit on any error

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
YAML_FILE="$SCRIPT_DIR/YAMLs/hyperexecute.yaml"

# Check if YAML file exists
if [ ! -f "$YAML_FILE" ]; then
    echo "Error: YAML file not found at $YAML_FILE"
    exit 1
fi

# Generate current timestamp in format: YYYY-MM-DD HH:MM:SS
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Create backup of original file
cp "$YAML_FILE" "$YAML_FILE.backup"

# Update the BUILD line with new timestamp
# Using sed to replace the BUILD line while preserving the YAML structure
# The pattern matches "BUILD: " followed by any characters
sed -i.tmp "s/^  BUILD: .*/  BUILD: $TIMESTAMP/" "$YAML_FILE"

# Remove temporary file created by sed
rm -f "$YAML_FILE.tmp"

echo "✅ Successfully updated BUILD timestamp to: $TIMESTAMP"
echo "📁 Original file backed up as: $YAML_FILE.backup"
echo "📄 Updated file: $YAML_FILE"

# Display the updated BUILD line for verification
echo "🔍 Updated BUILD line:"
grep "BUILD:" "$YAML_FILE"
