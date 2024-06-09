% first_script.m
% Example code using variables passed from the shell script

disp(['Variable 1: ', var1]);
disp(['Variable 2: ', var2]);

% Generate some data
data = rand(100, 1);

% Save the data to a .mat file
save('output_from_first_script.mat', 'data');
