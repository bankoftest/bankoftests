#!/bin/bash

# Step 1: Copy requirements.txt to docs/zh-CN
echo "Copying requirements.txt to docs/zh-CN..."
cp requirements.txt docs/zh-CN/

# Step 2: Clean the build directory
echo "Cleaning the build directory for zh-CN..."
rm -rf docs/zh-CN/build

# Step 3: Run the Python script to generate RST files
echo "Running generate_rst.py..."
python generate_rst.py

# Step 4: Build the HTML for zh-CN
echo "Building the HTML for zh-CN..."
make -C docs/zh-CN html

# Step 5: Open the generated index.html
echo "Opening the generated zh-CN index.html..."
open docs/zh-CN/build/html/index.html  # For MacOS