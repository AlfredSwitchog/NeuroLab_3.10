#!/bin/bash
#SBATCH --job-name=fmri_processing      # Job name
#SBATCH --output=output_%A_%a.txt       # Standard output and error log (%A for array job ID, %a for array task ID)
#SBATCH --ntasks=1                      # Run a single task per job --> defaults to 1 if not specified
#SBATCH --time=02:00:00                 # Time limit hrs:min:sec (estimate for one participant)
#SBATCH --mem=4G                        # Memory limit (estimate for one participant)
#SBATCH --array=1-100                   # Job array with 100 tasks (adjust based on the number of participants)
#SBATCH --partition=short               # Partition name (use your system's partitions)
#SBATCH --cpus-per-task=1               #dont specify defaults to 1 anyways

# Load necessary modules
module purge #might make sense
module load some_module

echo STARTED on $(date) with ID = $SLURM_ARRAY_TASK_ID

echo WORKING on some/file/path$SLURM_ARRAY_TASK_ID

# Read the participant ID for this task
#${SLURM_ARRAY_TASK_ID} --> this generates the task ID  for a single task
PARTICIPANT_ID=$(sed -n "${SLURM_ARRAY_TASK_ID}p" participant_ids.txt)

echo "Processing participant $PARTICIPANT_ID on `hostname` at `date`"

# Run your processing command
./process_fmri_data.sh $PARTICIPANT_ID

echo "Finished processing participant $PARTICIPANT_ID with exit code $? at: `date`"
