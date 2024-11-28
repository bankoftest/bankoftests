#!/bin/bash

# run ./build_zh.sh

# Step 0: Generate requirements.txt
echo "Generating requirements.txt..."
pip3 freeze > requirements.txt

# Step 1: Copy requirements.txt to docs/en
echo "Copying requirements.txt to docs/en..."
cp requirements.txt docs/en/

# Step 2: Clean the build directory
echo "Cleaning the build directory for en..."
rm -rf docs/en/build

# Step 3: Run the Python script to generate RST files
echo "Running generate_rst.py..."
python generate_rst.py

# Step 4: Build the HTML for en
echo "Building the HTML for en..."
make -C docs/en html

# Step 5: Open the generated index.html
echo "Opening the generated en index.html..."
open docs/en/build/html/index.html  # For MacOS
# xdg-open docs/en/build/html/index.html # Uncomment for Linux
# start docs/en/build/html/index.html    # Uncomment for Windows