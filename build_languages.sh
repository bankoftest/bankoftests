#!/bin/bash

# Define languages
languages=("en" "zh-CN")

# Loop through languages and build
for lang in "${languages[@]}"; do
    sphinx-build -b html -D language=$lang source build/html/$lang
done