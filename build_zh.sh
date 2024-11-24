#!/bin/bash

# Step 1: Copy requirements.txt to docs/zh-cn
echo "Copying requirements.txt to docs/zh-cn..."
cp requirements.txt docs/zh-cn/

# Step 2: Clean the build directory
echo "Cleaning the build directory for zh-cn..."
rm -rf docs/zh-cn/build

# Step 3: Run the Python script to generate RST files
echo "Running generate_rst.py..."
python generate_rst.py

# Step 4: Build the HTML for zh-cn
echo "Building the HTML for zh-cn..."
make -C docs/zh-cn html

# Step 5: Open the generated index.html
echo "Opening the generated zh-cn index.html..."
open docs/zh-cn/build/html/index.html  # For MacOS