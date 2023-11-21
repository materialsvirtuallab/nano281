---
layout: default
title: Lab 3 NANO281
parent: Assignments
nav_order: 4
---

# Introduction

Welcome to the final lab of NANO181 - Data Science in Materials Science. Unlike previous labs, this lab is deliberately more open-ended. You are encouraged to exercise your creativity in finding the best solutions.


# Getting started

Same as the previous lab, you need to set up your computer environment before the lab. 

1. Activate your NANOx81 virtual environment.

```bash
conda activate NANOx81
```
2. Start a Jupyter notebook.

```bash
jupyter notebook
```
3. Create a Python 3 notebook and rename it `NANOx81-lab3-<first_name>-<last_name>`.

# Assessment criteria

Try to complete all questions, doing everything in your Jupyter notebook. Make generous use of code cells, text cells, 
etc. and write your notebook as though it is a lab report but with Python code incorporated. The easier you make it for
your instructors to find the answers, the better.

At the end of the lab, please submit the `NANOx81-lab3-<first_name>-<last_name>.ipynb` file.

Just a reminder on our assessment criteria:
- Model performance: 30%
- Materials Science Insights: 30%
- Data Science Technique: 30%
- Programming Style: 10%

**You should ensure that any notebook you submit for your labs can be executed completely without errors.** The easiest
way to do this is to do a "Restart and Run All" from the notebook, which will execute all cells in your Jupyter notebook.

# Lab

Now that we are at the Final Lab, hints will be minimal. It is expected that your ML models are properly trained using best practices, your notebooks are clearly annotated and your code is Pythonic. All these will be accounted for in your final score.

## Problem

In this lab, you will train ML models to predict the `formation_energy_per_atom` of oxides in the Materials Project. Unlike the similar problem in Lab 2, there are a few complications:
1. The number of elements is not limited to 2. Each formula can have any number of elements.
2. The dataset is much larger (> 70,000 data points).

To ensure all students are working on the same data, the data has been pre-downloaded for you and separated into two sets: `train_oxides.csv` and `test_oxides.csv`. You do **not** need to create a test set. Answer the following questions (points in brackets are indicative score allocations):

1. (4 points) Download the files from the `Data` tab in the Kaggle site. Read the `train_oxides.csv` file into a Pandas DataFrame.
2. (70 points) Train the best possible model you can to predict `formation_energy_per_atom` from **compositional and structural** features. Here are the guidelines:
    a. For compositional features,while you can reuse the same `element_data.csv` file from lab 2, you should try to get more features from pymatgen's Element object. The features are documented [here](https://pymatgen.org/pymatgen.core.html#pymatgen.core.periodic_table.Element). Think carefully about what kind of features you should be using and what kind of processing you can use (min, max, weighted average, etc.). Note that reusing `element_data.csv` and just copy and pasting what you have from lab 2 will not result in good model performance or a good grade.
    b. Though obtaining structures require relaxations, nowadays such relaxations can be performed using universal potentials such as [M3GNet](http://matgl.ai). You can use the Materials Project API to query for such features for now. Examples include the density, space group, positions of atoms, etc. Note that not all features will make sense and you are expected to figure out what features to use. Alternatively, you can use the Materials Project API to query for structures and then generate your own structural features. You can also use generate features using [matminer](https://github.com/hackingmaterials/matminer) or [universal potentials](http://matgl.ai). Note that you are allowed to use *structural* information only, not other information you obtain from a DFT calculation.
Upload the predictions of your best model to the Kaggle site. Look at the file called `sample_submission.csv` to understand the format of the file that needs to be submitted. You just need two columns - `material_id` and `formation_energy_per_atom`.  You can make multiple uploads daily over the course of the lab. What is the test MAE for your best model? It should be stressed that NANO281 Lab 3 is more like a mini-research project. We expect to see good effort made at attempting to solve the problem. In particular,  for graduate students, we need to see an attempt to use structural features, not just compositional ones.
3. (26 points) Perform analyses of which features contribute to the prediction of `formation_energy_per_atom` for your best models. Interpret the results using your materials science knowledge.


Important notes on expectations:

1. We expect to see you apply all that you have learnt in NANOx81. That includes proper use of cross-validation for model selection, hyperparameter tuning for each of your models (plots showing loss function/score against hyperparameters are expected). Note that we can only grade based on what we see in your submitted notebook. Simply sending in your models with no evidence of all these efforts will not result in a good grade, regardless of how well the models perform.
2. We expect at least one Kaggle prediction upload per week from all students. One in week 1 and another in week 2. You are free to upload more often if you wish.
3. Model performance is 30% of your grade. Since this is the final lab in a data science class, we will use statistial approaches to assign this grade. We will take the average MSE of all NANO181 models and use it to assign a score for this aspect.
4. Since this is the final lab, we are expecting well-written code with clear documentation on every step. Explain your thinking behind every single thing you do. Use Jupyter's markdown cells to present your thought processes. Make plots to show key analyses.

