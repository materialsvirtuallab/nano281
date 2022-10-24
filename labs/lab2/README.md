# Introduction

Welcome to Lab 2 of NANOx81 - Data Science in Materials Science. So far you should already have basic knowledge of
python data science stack and know how to manipulate materials data. In this lab, it is time to put your knowledge into
use. We will be solving real materials research problems - using both theoretically computed as well as experimental
data using data science techniques. 

# Getting started

Same as previous lab, you need to set up your computer environment before the lab. You may alternatively use
[Google Colab](https://colab.research.google.com/) to do this lab, in which case you can skip directly to step 3.

1. Activate your NANOx81 virtual environment.
```bash
conda activate NANOx81
```

2. Start a Jupyter notebook.
```bash
jupyter notebook
```

3. Create a Python 3 notebook and rename it `NANOx81-lab2-<first_name>-<last_name>`.

# Assessment criteria
Try to complete all questions, doing everything in your Jupyter notebook. Make generous use of code cells, text cells, 
etc. and write your notebook as though it is a lab report but with Python code incorporated. The easier you make it for
your instructors to find the answers, the better.

**At the end of the lab, please submit the `NANOx81-lab2-<first_name>-<last_name>.ipynb` file via Canvas.**

Just a reminder on our assessment criteria:
- Model performance: 30%
- Materials Science Insights: 30%
- Data Science Technique: 30%
- Programming Style: 10%

**You should ensure that any notebook you submit for your labs can be executed completely without errors.** The easiest
way to do this is to do a "Restart and Run All" from the notebook, which will execute all cells in your Jupyter notebook.

# Lab

Download `data2022.csv` file in this repo. It contains some data for all binary bromides and iodides in the Materials
Project.

## Q1 - Exploratory data analysis (7 points)

Load the `data2022.csv` in variable `orig_data` using `pandas.read_csv` with `na_filter=False` option, and perform the
following analysis. 

1. How many materials are there in this dataset? (1 point)
2. How many elements are there in this data set? (1 point)
3. How many unique formulae are there? (1 point)
4. Count the number of materials where each element is present. Sort this count. Create a barplot showing the
   number of materials with the top 10 most common elements in this data set. (4 points)

Hint: When dealing with formula, you may use `pymatgen.core.Composition` to speed up the process. For example, the
following code snippet shows the use of Composition to process formula. For more usage, you may visit
[https://matgenb.materialsvirtuallab.org/2013/01/01/Basic-functionality.html](https://matgenb.materialsvirtuallab.org/2013/01/01/Basic-functionality.html) 

```python
from pymatgen.core import Composition
comp = Composition('Al2O3')
print(comp.elements)  # this will give you the elements
print(comp.to_data_dict['unit_cell_composition'])  # this will give you the elementstr-stoichiometry dictionary.
```
## Q2 - Data cleaning and feature computations (24 points)

About 80% of the effort in ML modelling is in data processing. The goal is to develop ML models to predict the formation
energy per atom and band gap of the material from the formula. To do that, we will first convert the formula to numeric
vectors (descriptors) for model inputs. For data filtering steps, note that you should use the filtered data after each
filtering step henceforth.

1. From Q1.3, we note that the number of materials is greater than the number of formulae, i.e., there can be more than
   1 polymorph present per formula. We do not expect the compositional features to be able to predict multiple values
   of the same property for the same formula. Filter the data to remove duplicate formulae, keeping only the row with
   the lowest formation energy per atom for each formula. How many materials are left? (2 points)
2. Positive formation energies are often a sign that a calculation is poorly converged. Filter the data to remove rows
   with positive formation energies as well. How many materials are left? (2 point)
3. Load the element property data file `element_properties.csv` in variable `element_data` using pandas by setting
   `index_col=0` in `pandas.read_csv` function. How many NaN (Not a Number) are there in each column? (1 point)
4. Compute the mean values for each column, ignoring the NaNs. For each column, fill the NaN with the mean value of
   that column. This is a common data imputation technique. (2 points)
5. Compute the composition-averaged `AtomicRadius` for all materials and store the results in variable `atomic_radius`.
   For example, averaged `AtomicRadius` for `Li2O` can be computed as `(2 * 1.45 + 0.6) / 3`, where `1.45` is the
   `AtomicRadius` for `Li` and `0.6` is the `AtomicRadius` for `O`. (5 points)
6. Compute the composition-averaged properties for all properties in `element_data` and for all materials. Store the 
   results in the variable `average_properties`. `average_properties` should have a dimension of `(n, 11)` where `n` is
   the number of materials and 11 is the number of properties. (5 points)
7. Similar to the previous computations of average properties, compute the maximum properties and minimum properties for
   all properties and all materials, and store them in variables `max_properties` and `min_properties` respectively.
   Both variables should have dimension `(n, 11)`. (5 points)
8. Concatenate `average_properties`, `max_properties` and `min_properties`, and store the result in variable
   `design_matrix` with dimension `(n, 33)`. (2 point)

## Q3 - Regression and classification modeling (46 points)

We are going to use `band_gap` and `formation_energy_per_atom` in `data` as the targets. To make sure the results are
reproducible, set the `random_state=42` in all cases where random sampling is involved, e.g., train_test_split,
shuffling, etc.

1. Split the data (`design_matrix` as X, and `targets` as y) into training and test sets in the ratio 90%:10%. Store
   the training data in variables `train_X` and `train_y` and the test data as variables `test_X` and `test_y`.
   (2 points)
2. Compute the mean and standard deviation of columns in `train_X`. Both of them should be length 33 vectors. Use them
   to normalize `train_X` and `test_X`, so that each column has a mean of 0 and standard deviation of 1. Store the
   normalized design matrices to `norm_train_X`, `norm_test_X`. (4 points)

Note that from here out, all model training and validation should be done with the training split and all reported
test results should be done using the test split. You should be using proper ML best practices such as cross-validation
in fitting the model. In all cases, the loss function you use should be the mean squared error. You need to figure out
where and how to specify the loss function in the training.

3. Train a simple linear regression model to predict `formation_energy_per_atom`. What is the CV score of your model?
   (4 points)
4. Train a Ridge regression model and a LASSO regression model for the `formation_energy_per_atom`. You need to search
   for an optimal value of `alpha`. To help you, try the following ranges of alpha: ridge (0.1-10), lasso (0.0001-0.01).
   You have to figure out how best to sample the range of alphas. Too dense a sampling will result in very slow searches
   and too sparse will result in non-optimal models. What are the CV scores of your best Ridge and Lasso models?
   (13 points)
5. What are the test MAE and RMSE of the best model (among those you have fitted so far)? (2 points)
6. What are the features that do not contribute to the LASSO prediction? (4 points)
7. Let's define `band_gap < 0.001` as metallic and `band_gap >= 0.001` as nonmetallic. Construct linear discriminant
   analysis, quadratic discriminant analysis, and logistic regression models on train data and predict the accuracy of
   the models on test data. (15)
8. What are the problems of using only the compositions to predict material properties? (2 points)

## Q4 - Clustering (30 points)

In this problem, we will be looking at catalyst clusters. The image file `catalyst.png` below is extracted from a
figure shared on figshare by Gomez-Bolivar et al. (Front. Microbiol., 20 June 2019, DOI: 10.3389/fmicb.2019.01276). It
is an energy dispersive X-ray (EDX) microanalysis of Pd/Ru bimetallic nanoparticle catalysts synthesized by
Escherichia coli. For this whole exercise, it is recommended that you use the `hot` colormap in matplotlib.

![catalyst.png](catalyst.png "catalyst.png")

1. Read in the image as a numpy array using matplotlib. Show the image in your Jupyter notebook. What are the
   dimensions of the array? (1 point)
2. Plot the distribution of the values in the numpy array representing the image. Note that the values in the numpy
   array are between zero and 1. (1 point)
3. Measured images has a variety of levels. Sometimes, we want to label each pixel at pre-specified levels, e.g., 0
   representing the background, and fixed values representing certain features. This is known as vector quantization.
   Here, we will quantize the image using K-means. We know for a fact that there are two elements (Pd and Ru) in the
   system. Using K-means, quantize the image such that there are three levels: 0 = background, 1 and 2 = Pd or Ru.
   Ensure that 0 corresponds to the background (this should be the cluster with the largest number of data points) and
   non-zero levels correspond to the elements. Plot the quantized image. (6 points)
4. For the purposes of this exercise, we will not attempt to distinguish between different elements. Any value within
   the numpy array that is > 0 is considered a catalyst particle. Use K-means clustering to identify
   clusters of metal particles (you will need to figure out what a good value of K is). Plot your clustered image,
   ensuring that each cluster has a different color. Comment on how you chose your value of K. (10 points)
5. Finally, we will use a density-based clustering method called DBSCAN. Similar to part 4, any value in the numpy
   array that is > 0 is considered a catalyst particle. Use DBSCAN clustering to distinguish identify clusters of metal
   particles (you will need to figure out what a good value of `eps` is). Plot your clustered image, ensuring that each
   cluster has a different color. Comment on how you chose your value of `eps`. (10 points)
6. Discuss on the differences between the K-means and DBSCAN results, and which method is more appropriate for the
   purpose we are using it for. (2 points)
