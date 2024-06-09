#!/bin/bash

# Define variables
var1="value1_test_RL"
var2="value2"

# Execute the first MATLAB script with variables
echo "Running first MATLAB script..."
matlab -arch=maci64 -nodisplay -nosplash -r "var1='$var1'; var2='$var2'; run('Preprocessing_test_1.m'); exit;"

# Check if the first MATLAB script executed successfully
if [ $? -ne 0 ]; then
    echo "First MATLAB script failed!"
    exit 1
fi

# Execute the second MATLAB script with variables
echo "Running second MATLAB script..."
matlab -arch=maci64 -nodisplay -nosplash -r "var1='$var1'; var2='$var2'; run('Preprocessing_test_2.m'); exit;"

# Check if the second MATLAB script executed successfully
if [ $? -ne 0 ]; then
    echo "Second MATLAB script failed!"
    exit 1
fi
