import numpy as np
import os
from nilearn import image, plotting
from nilearn.image import new_img_like
import matplotlib as mpl
import matplotlib.pyplot as plt

# set Output folder of LayNii Outputs
output_folder = '/Users/Richard/LayNii/Output/'

# From Outputfolder only select overall_correl files --> Why?
scans_mean = [file for file in os.listdir(output_folder) if file.endswith("overall_correl.nii")]

# Question: Is selecting only specific files only relevant when we have more then one overall_correl file?
positions_to_select36 = [2, 7, 4, 8]
positions_to_select72 = [3, 5, 1, 6, 0]

# Out of range error here when only one file is present
mylist36 = [scans_mean[idx] for idx in positions_to_select36]
mylist72 = [scans_mean[idx] for idx in positions_to_select72]

# load each nii file
for i, volume in enumerate(scans_mean):
    scan_data = image.load_img(os.path.join(output_folder + volume))

# This gives you the dimensions of the nifti image,
# the numbers represent the voxel count in each dimension (x,y,z)
# the last number representing the number of timepoints
print(scan_data.get_fdata().shape)

# set number of slices
slices = [10, 20, 30]

# create plot layout based on number of files provided and specified slices
fig, axes = plt.subplots(nrows=len(scans_mean), ncols=len(slices), figsize=(15, 10))

"""
for i, volume in enumerate(scans_mean):
    scan_data =image.load_img(os.path.join(output_folder + volume))

print(scan_data.get_fdata().shape)
"""

# select one slice from the original scanned data
scan_data_3d = new_img_like(scan_data, scan_data.get_fdata()[:, :, :, 0])

# iterating over each slice value, specified above
for j, slice_val in enumerate(slices):
    display = plotting.plot_anat(scan_data_3d,
                                 display_mode='z',
                                 cut_coords=[slice_val],
                                 black_bg=False,
                                 axes=axes[i, j])  # Access the specific ax using the 2D array indexing
# axes = axes[i,j] doesn't work --> too many axes are given

plt.show()

# Set the font family to Arial
plt.rcParams["font.family"] = "Arial"

slices = [10, 22, 42, 62]

row_titles = ["M", "M_MoCo", "E", "E_MoCo", "Lido"]
col_titles = ["slice 10", "slice 22", "slice 42", "slice 62"]

fig, axes = plt.subplots(nrows=len(mylist72), ncols=len(slices), figsize=(12, 20), sharex=True)  # Add sharex parameter

for i, volume in enumerate(mylist72):
    scan_data = image.load_img(os.path.join(output_folder + volume))
    scan_data_3d = image.new_img_like(scan_data, scan_data.get_fdata()[:, :, :, 0])

for j, slice_val in enumerate(slices):
    data_slice = scan_data_3d.get_fdata()[:, :, slice_val]
    # data_slice = data_slice.clip(min=0, max=80) # Clip the data to the range [0, 80]
    ax = axes[i, j]
    img = ax.imshow(data_slice, vmin=0, vmax=80, cmap='inferno')