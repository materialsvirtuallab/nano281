# Introduction

Welcome to Lab 1 of NANO281 - Data Science in Materials Science. In this lab, you will be learn how to handle materials data using various open-source Python tools.

# Getting started

Before starting on the lab, please ensure that you have your Python environment setup properly. If you have not already done so, please follow the following steps:

1. Download the Python 3.7+ version of [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (recommended) or [Anaconda](https://www.anaconda.com/distribution/) for your OS.
2. Follow the official instructions adn install Miniconda/Anaconda.
3. Start the terminal (Mac/Linux) or Anaconda Prompt (Windows).
4. Create a virtual environment for NANO281:
```bash
conda create --name nano281 python=3.7
```
5. Activate the virtual environment.
```bash
conda activate nano281
```
6. Install the necessary Python libraries.
```bash
conda install --yes numpy scipy matplotlib pandas jupyter seaborn scikit-learn tensorflow pymatgen
```
7. An alternative to steps 4-6 is to download the nano281_env.yml file from the Google classroom or Github repo and create the environment directly.
```bash
conda env create -f nano281_env.yml
```
8. Subsequently, always ensure that you are in the nano281 environment using `conda activate nano281` prior to working on your labs.
9. Start a Jupyter notebook
```bash
jupyter notebook
```
10. Create a notebook and rename it `nano281-lab1-<first_name>-<last_name>`.



