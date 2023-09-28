---
layout: default
title: Python Setup
nav_order: 3
---

# Setting up your own Python environment

If you are not using Google Colab, you will need to setup a working Python environment with all the necessary 
dependencies. You only need to do this once. There are alternative approaches to setting up your machine, but the 
approach outlined here is guaranteed to work and is reproducible. Your instructors would be better able to assist if 
there are issues in the installation.

1. Download the Python 3.11+ version of [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 
   (recommended) or [Anaconda](https://www.anaconda.com/distribution/) for your OS.
2. Follow the official instructions and install Miniconda/Anaconda.
3. Start the terminal (Mac/Linux) or Anaconda Prompt (Windows).
4. Create a virtual environment for NANO181/281:
```bash
conda create --name NANOx81 python=3.11
```
5. Activate the virtual environment.
```bash
conda activate NANOx81
```
6. Install the necessary Python libraries.
```bash
conda install --yes numpy scipy matplotlib pandas jupyter seaborn scikit-learn
conda install --channel conda-forge --yes pymatgen
```
7. An alternative to steps 4-6 is to download the [nanox81_env.yml](https://raw.githubusercontent.com/materialsvirtuallab/NANO281/master/nanox81_env.yml) 
   file from the Github repo and create the environment directly.
```bash
conda env create -f nanox81_env.yml
```
8. Subsequently, always activate your NANO181/281 environment prior to working on
   your lectures/labs using:
```bash
conda activate NANOx81
```

If for any reason you find that your conda environment is corrupted and you
need to start over, please run:
```bash
conda env remove --name NANOx81
```
and simply start from step 4 above to redo your setup.
