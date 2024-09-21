
# Introduction

This repository holds the code for the publication: [Lee et al. JCIM (2024)](https://pubs.acs.org/doi/full/10.1021/acs.jcim.3c01583#).

The dependencies for running these scripts include:
* rdkit
* numpy
* pandas
* matplotlib 

The code here should be sufficient for reproducing the main paper figures. To reproduce all figures, please follow the following steps. Numbered scripts within a directory should be run in numerical order.


1. First compute Emin from scratch for the QM9 dataset, by running the scripts in numbered order within the directory **Computing Emin for QM9**. You will first need to download files within the links found in **Computing Emin for QM9/data/raw/README.md**
2. Next, compute other synthesizabaility scores for the QM9 dataset by running all scripts within **Computing Other Scores**. Each script will take the output from step 1, calculate the corresponding score, and overwrite the file from step 1 with the additional score.
    - install ASKCOS from here: https://github.com/ASKCOS/askcos-core/tree/main and specify the installation path at the top of sa_sc_syba_score_parallel.py
    - install RA score from here: https://github.com/reymond-group/RAscore
    - install SYBA score from here: https://github.com/lich-uct/syba

3. Use the Mordred descriptor calculator in **Computing Mordred Features for QM9** to compute general descriptors for ML. This will take the file from step 1 (now with all calculated other scores from step 2), calculate Mordred descriptors, and write a new file to this step's directory.
    - install Mordred from here: https://github.com/mordred-descriptor/mordred
4. Open **Reproduce paper figures** and run each script in any order. 

## Computing E<sub>min</sub> on New Molecules

We have also made an application for evaluating E<sub>min</sub> on arbitrary molecules: https://github.com/HydrogenStorage/molecular-stability-computer
