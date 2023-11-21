---
layout: default
title: Lab 3 NANO181
parent: Assignments
nav_order: 3
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

Now that we are at the Final Lab, hints will be minimal. It is expected that your ML models are
properly trained using best practices, your notebooks are clearly annotated and your code is Pythonic. All these will be accounted for in your final score.

## Problem

In this lab, you will train ML models to predict the `formation_energy_per_atom` of oxides in the Materials Project. Unlike the similar problem in Lab 2, there are a few complications:
1. The number of elements is not limited to 2. Each formula can have any number of elements.
2. The dataset is much larger (> 70,000 data points)


To ensure all students are working on the same data, the data has been pre-downloaded for you and separated into two sets: `train_oxides` and `test_oxides`. You do **not** need to create a test set. Answer the following questions (points in brackets are indicative score allocations):

1. (5 points) Download the files from the `Data` tab in the Kaggle site. Read the `train_oxides.csv` file into a Pandas DataFrame.
2. (5 points) Plot histograms of `formation_energy_per_atom`.  
3. (10 points) Generate **composition-based features** (similar to what you have done in lab 2). While you can reuse the same `element_data.csv` file from lab 2, you should try to get more features from pymatgen's Element object. The features are documented [here](https://pymatgen.org/pymatgen.core.html#pymatgen.core.periodic_table.Element). Think carefully about what kind of features you should be using and what kind of processing you can use (min, max, weighted average, etc.). Note that reusing `element_data.csv` and just copy and pasting what you have from lab 2 will not result in good model performance or a good grade.
4. (20 points) Train a simple linear type model with shrinkage/regularization and/or feature transformations to predict `formation_energy_per_atom`. Upload the predictions of your best model to the Kaggle site. Look at the file called `sample_submission.csv` to understand the format of the file that needs to be submitted. You just need two columns - `material_id` and `formation_energy_per_atom`.  You can make multiple uploads over the course of the lab. What is the test MSE for your best model? 
5. (30 points) Train a tree-based model to predict `formation_energy_per_atom`. Same as before, upload the predictions of your best model to Kaggle. What is the MSE on your test set for your best model? 
6. (10 points) Do a simple 80:20 split on the training data. Train your model using the 80% split and the best model parameters foud (either linear or tree based). Plot the predicted vs actual `formation_energy_per_atom` for the 80% training data and 20% test data. Annotate your plot with the MSEs for the training and test set.
7. (20 points) Perform analyses of which features are important to the prediction of `formation_energy_per_atom` for your best linear and tree-based models. Interpret the results using your materials science knowledge. Discuss which model performs better and why? 

Important notes on expectations:

1. We expect to see you apply all that you have learnt in NANOx81. That includes proper use of cross-validation for model selection, hyperparameter tuning for each of your models (plots showing loss function/score against hyperparameters are expected). Note that we can only grade based on what we see in your submitted notebook. Simply sending in your models with no evidence of all these efforts will not result in a good grade, regardless of how well the models perform.
2. We expect at least one Kaggle prediction upload per week from all students. One in week 1 and another in week 2. You are free to upload more often if you wish.
3. Model performance is 30% of your grade. Since this is the final lab in a data science class, we will use statistial approaches to assign this grade. We will take the average MSE of all NANO181 models and use it to assign a score for this aspect.
4. Since this is the final lab, we are expecting well-written code with clear documentation on every step. Explain your thinking behind every single thing you do. Use Jupyter's markdown cells to present your thought processes. Make plots to show key analyses.
