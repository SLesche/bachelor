#!/bin/bash
#SBATCH --job-name=no-bias
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2gb
#SBATCH --mail-type=end
#SBATCH --mail-user=sven.lesche@stud.uni-heidelberg.de
#SBATCH --output=no_bias

module load math/R/4.1.2
module load devel/tbb/2021.4.0
export TBB_LIB=$TBB_LIB_DIR
export TBB_INC=$TBB_INC_DIR
export TBB_INTERFACE_NEW='true'
Rscript bachelor/no_bias.R