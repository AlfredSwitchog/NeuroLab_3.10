#!/bin/bash
SBATCH --job-name=fmri_processing    # Job name
SBATCH --output=job_%A_%a.out       # Output file (includes job array task ID)
SBATCH --error=job_%A_%a.err        # Error file (includes job array task ID)
SBATCH --partition=compute           # Queue (partition) name
SBATCH --nodes=1                     # Number of nodes
SBATCH --ntasks=1                    # Number of tasks (processes) per job
SBATCH --cpus-per-task=4             # Number of CPU cores per task
SBATCH --mem=4G                      # Memory per node
SBATCH --array=1-5                   # Number of participants

# Load any necessary modules
module load my_module

# Define participant IDs and data folders
participants=(1 2 3 4 5)
data_folders=("participant_1_data" "participant_2_data" "participant_3_data" "participant_4_data" "participant_5_data")

# Get the participant ID and data folder for this job
participant_id=${participants[$SLURM_ARRAY_TASK_ID - 1]}
data_folder=${data_folders[$SLURM_ARRAY_TASK_ID - 1]}

# Run your fMRI processing script for the current participant's data
python process_fmri.py --data_folder $data_folder
