#!/bin/bash
#SBATCH --job-name=pred-location-base
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mail-type=end
#SBATCH --mail-user=sven.lesche@stud.uni-heidelberg.de

module load math/R/4.1.2
module load devel/tbb/2021.4.0
export TBB_LIB=$TBB_LIB_DIR
export TBB_INC=$TBB_INC_DIR
export TBB_INTERFACE_NEW='true'
Rscript bachelor/location_model_base_final_pred.R