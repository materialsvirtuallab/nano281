---
layout: default
title: Lab 1
parent: Assignments
nav_order: 1
---

# Introduction

Welcome to Lab 1 of NANOx81 - Data Science in Materials Science. In this lab, you will be learn how to handle materials
data using various open-source Python tools.

# Getting started

If you have not already done so, please follow the instructions outlined in the main [README](https://github.com/materialsvirtuallab/nano281)
to set up your computer. You may alternatively use [Google Colab](https://colab.research.google.com/) to do this lab,
in which case you can skip directly to step 3.

1. Activate your NANOx81 virtual environment.
```bash
conda activate NANOx81
```
2. Start a Jupyter notebook
```bash
jupyter notebook
```
3. Create a Python 3 notebook and rename it `NANOx81-lab1-<first_name>-<last_name>`. This is important because I expect 
   to be receiving a notebook from every student.

# Assessment criteria

Try to complete all questions, doing everything in your Jupyter notebook. Make generous use of code cells, text cells, 
etc. and write your notebook as though it is a lab report but with Python code incorporated. The easier you make it for
your instructors to find the answers, the better.

**At the end of the lab, please submit the `NANOx81-lab1-<first_name>-<last_name>.ipynb` file (it should be in whatever
directory you started your jupyter notebook application in) via Canvas.**

Just a reminder on our assessment criteria:
- Model performance: 30%
- Materials Science Insights: 30%
- Data Science Technique: 30%
- Programming Style: 10%

For this first lab, you will not be building any models. So the primary evaluation is based on the data science
technique and programming. **First and foremost, you should ensure that any notebook you submit for your labs can be
executed completely without errors.** The easiest way to do this is to do a "Restart and Run All" from the notebook,
which will execute all cells in your Jupyter notebook.

# Lab

We will explore various sources of materials data:
* Large public databases with API (Materials Project)
* Shared research data (figshare)

## Q1 - Materials Project data (38 points)

Using pymatgen (or any alternative approach), query the Materials Project for the following properties of all ABO3 type
compounds: 

- materials project identifier (material_id)
- formula of the compound
- number of sites in the unit cell
- band gap
- formation energy per atom
- theoretical (indicates whether a material is a theoretically generated one.)
- energy above hull

You will need to sign up for a free account at https://www.materialsproject.org and get an API_KEY from the
https://www.materialsproject.org/dashboard.

![API key](MP_API_KEY.png "Getting the Materials Project API key")

Hints:
- Go back to the lecture 1 example notebook for a quick starting example.
- The Materials Project API Documentation also has [examples](https://docs.materialsproject.org/downloading-data/using-the-api/examples)
  that can make this go faster. Focus on summary queries.
- You will also need to refer to the [API docs](https://api.materialsproject.org/docs) to understand what the summary
  doc contains. Note that you will need to figure out what is the name of the fields you need to be querying!

Answer the following questions:

1. Perform the query and convert the data into a Pandas DataFrame. (10 points)
2. How many ABO3 compounds in total are there in the Materials Project? How many unique ABO3 formulae are there? What
   is the average number of crystals (also known as polymorphs) per ABO3 formula? (6 points)
3. What fraction of the compounds are non-theoretical? (2 points)
4. The formation energies in the Materials Project are given in eV/atom. Create an additional column in your dataset
   that has the formation energies in J/mol. (4 points)
5. Let us assume that materials with energy above hull of >0.03 eV/atom are `unstable` and are `potentially stable`
   otherwise. Furthermore, band gaps (E_g) of E_g = 0, 0 < E_g ≤ 1, E_g > 1 are indicative of `metallic`, 
   `small band gap`, `large band gap` for the materials. Create a table of the number of ABO3 crystals in each joint
   category, e.g., `(unstable, metallic)`, `(unstable, small band gap)`, etc. (10 points)
6. Plot the distribution of (a) the formation energies per atom (in eV/atom) and (b) the band gaps of all the materials.
   Annotate the plots with the average and standard deviation of each quantity. Ensure that all axes are labelled
   appropriately with units, i.e., something that you6 can potentially put in a scientific paper. (6 points)


## Q2 - Publicly available research data (30 points)

Researchers frequently share the datasets they have via various online platforms. [Figshare](https://figshare.com/) is
one such online platform. We will use this example to illustrate some of the challenges in working with datasets.

1. Query for the data from https://ndownloader.figshare.com/files/9158587, which is in the csv format. This is a dataset
   of from high-throughput DFT calculations of formation energy, stability and oxygen vacancy formation energy of ABO3
   perovskites (https://www.nature.com/articles/sdata2017153) available in the Open Quantum Materials Database (OQMD).
   This dataset, which we will call the OQMD dataset, comprises computed data on compounds known as perovskites. Parse
   the data into a Pandas DataFrame. (10 points)
2. How many compounds in total are there? (2 points)
3. How many total columns are there in the dataset? Print the column names. (2 points)
4. Unfortunately, the dataset contains invalid data and some of the data are also not properly tagged in the right data
   type. For example, the formation energy column contains strings, rather than floating point numbers. There are also
   strings that indicate whether a particular data point is valid. Filter the DataFrame to remove all invalid data
   points, i.e., those that contain just "-" in the formation energy column. and convert the formation energy column to
   the proper floats. How many data points remain? (10 points)
5. Plot the distribution of the formation energies per atom. Annotate the plot with the average and standard deviation.
   (6 points)

## Q3 - Comparing data sets (32 points)

It is often useful to compare similar datasets to check them against each other. The simplest form of the perovskite
crystal structure has formula ABO3, and such compounds are present in both the dataset you queried from the Materials
Project in Q1 and the OQMD data you downloaded from figshare in Q2.

1. Identify the subset of formulas that are present in both the Materials Project dataset and OQMD dataset (hint: look
   at the Python built-in `set` object). How many formulas are there? (10 points)
2. Plot the distribution of the formation energies per atom of this subset of formulas for (a) the Materials Project
   dataset, and (b) the OQMD data, overlaying the two distributions on top of each other. Annotate your plot with the
   mean and standard deviation for each data set. (10 points)
3. Perform a hypothesis test at the 95% level to determine if there is a significant difference between the formation
   energies reported in the Materials Project and the OQMD dataset (hint: check out the scipy.stats.ttest_ind method).
   Discuss your findings, including providing any possible explanations for any discrepancy between the two datasets.
   (12 points)
