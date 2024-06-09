#!/bin/bash

# Define variables
var1="value1"
var2="value2"

# Execute the first MATLAB script with variables
echo "Running first MATLAB script..."
matlab -nodisplay -nosplash -r "var1='$var1'; var2='$var2'; run('first_script.m'); exit;"

# Check if the first MATLAB script executed successfully
if [ $? -ne 0 ]; then
    echo "First MATLAB script failed!"
    exit 1
fi

# Execute the second MATLAB script with variables
echo "Running second MATLAB script..."
matlab -nodisplay -nosplash -r "var1='$var1'; var2='$var2'; run('second_script.m'); exit;"

# Check if the second MATLAB script executed successfully
if [ $? -ne 0 ]; then
    echo "Second MATLAB script failed!"
    exit 1
fi

# Execute the Laynii command
echo "Running Laynii command..."
laynii_command="LN_FUNC_DOTPRODUCT -input1 output_from_first_script.nii -input2 output_from_second_script.nii -output dot_product_output.nii"
eval $laynii_command

# Check if the Laynii command executed successfully
if [ $? -ne 0 ]; then
    echo "Laynii command failed!"
    exit 1
fi

# Execute the Python script to generate images
echo "Running Python script..."
python generate_images.py dot_product_output.nii

# Check if the Python script executed successfully
if [ $? -ne 0 ]; then
    echo "Python script failed!"
    exit 1
fi

echo "Pipeline executed successfully!"
