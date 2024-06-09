% second_script.m
% Example code using variables passed from the shell script

disp(['Variable 1: ', var1]);
disp(['Variable 2: ', var2]);

% Load the data from the .mat file
load('output_from_first_script.mat', 'data');

% Process the data
processed_data = data * 2;

% Save the processed data to another .mat file
save('output_from_second_script.mat', 'processed_data');
