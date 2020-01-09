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
10. Create a notebook and rename it `nano281-lab1-<first_name>-<last_name>`. This is important because I expect to be receiving a notebook from every student.


# Assessment criteria

Just a reminder on our assessment criteria for labs.
- Model performance: 30%
- Materials Science Insights: 30%
- Data Science Technique: 30%
- Programming Style: 10%

For this first lab, you will not be building any models. So the primary evaluation is based on the data science technique and programming. **First and foremost, you should ensure that any notebook you submit for your labs can be executed completely without errors.** The easiest way to do this is to do a "Restart and Run All" from the notebook, which will execute all cells in your Jupyter notebook.


# Lab

We will explore various sources of materials data:
* Large public databases with API (Materials Project)
* Shared research data (figshare)

## Q1 - Materials Project data

Using pymatgen (or any alternative approach), query the Materials Project for the following properties of all ABO3 type compounds (hint: look at this [example notebook](https://github.com/materialsproject/mapidoc/blob/master/example_notebooks/Using%20the%20Materials%20API%20with%20Python.ipynb) and figure out what is the best way to do this) compounds: materials project identifier, formula of the compound, number of sites in the unit cell, band gap, formation energy per atom, icsd ids, energy above hull. You will need to sign up for a free account at https://www.materialsproject.org and get an API_KEY from the https://www.materialsproject.org/dashboard . 1. Perform the query and convert the data into a Pandas DataFrame.

![API key](MP_API_KEY.png "Getting the Materials Project API key")

Answer the following questions:
1. How many ABO3 compounds in total are there?
2. Typically, the existence of an ICSD (Inorganic Crystal Structure Database) id is a rough indication of whether a compound is an experimentally-known compound or a theoretical compound. What fraction of the compounds have at least one icsd id?
3. The formation energies in the Materials Project are given in eV/atom. Create an additional column in your dataset that has the formation energies in J/mol.
4. Plot the distribution of (a) the formation energies per atom (in eV/atom) and (b) the band gaps of all the materials. Annotate the plots with the average and standard deviation of each quantity. Ensure that all axes are labelled appropriately with units, i.e., something that you can potentially put in a scientific paper.


## Q2 - Publicly available research data

1. Query for the data for perovskites from https://ndownloader.figshare.com/files/12978425, which is in the csv format. Parse the data into a Pandas DataFrame.
2. How many compounds in total are there?
3. How many total columns are there in the dataset?
4. Plot the distribution of the formation energies per atom. Annotate the plot with the average and standard deviation.

