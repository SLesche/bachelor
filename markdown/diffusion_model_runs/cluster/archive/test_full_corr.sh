#!/bin/bash
#SBATCH --job-name=full_cor_test
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mail-type=all
#SBATCH --mail-user=sven.lesche@stud.uni-heidelberg.de
#SBATCH --output=test_full_cor

module load math/R/4.1.2
module load devel/tbb/2021.4.0
export TBB_LIB=$TBB_LIB_DIR
export TBB_INC=$TBB_INC_DIR
export TBB_INTERFACE_NEW='true'
Rscript bachelor/test_full_corr.R