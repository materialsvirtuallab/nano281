---
layout: default
title: Home
nav_order: 1
---

# NANO181/281 - Data Science in Materials Science

Welcome to the UCSD Course NANO 181/281 - "Data Science in Materials Science".

# Syllabus

The full syllabus is provided [here](syllabus).

# Lecture materials

## Slides

1. [Course Admin](assets%2Fslides%2F00-Course_Admin.pdf)
2. [Python for Data Science](assets%2Fslides%2F01-Python_for_Data_Science.pdf)
3. [Data Science in Materials Science](assets%2Fslides%2F02-Introduction_to_Data_Science_in_Materials_Science.pdf)
4. [Linear Methods](assets%2Fslides%2F03-Linear_Methods.pdf)
5. [Improving and extending linear models](assets%2Fslides%2F04-Improving_and_extending_linear_models.pdf)
6. [Linear Classification](assets%2Fslides%2F05-Linear_Classification.pdf)
7. [Unsupervised Learning](assets%2Fslides%2F06-Unsupervised_Learning.pdf)
8. [Kernel Regression](assets%2Fslides%2F07-Kernel_Regression.pdf)
9. [Generalized Additive Models and Trees](assets%2Fslides%2F08-Generalized_Additive_Models_and_Trees.pdf)
10. [Neural Networks](assets%2Fslides%2F09-Neural_Networks.pdf)

## Jupyter Notebooks

In-lecture demos will be conducted using Jupyter notebooks, available [here](https://github.com/materialsvirtuallab/nano281/tree/master/lectures/notebooks).

# Labs

There are three lab sessions. The instructions for the first two labs are available via the menu on the left. The 
final lab will be an open problem that will be determined at a later date and will be held via a Kaggle competition.

# Programming language

All lectures and labs will be conducted in Python 3.9+. Prior to the labs,
please do the following:

1. Install [python](https://www.python.org/) on your laptop (see next section).
2. If you are unfamiliar with Python, please go through the official
   [Python tutorials](https://docs.python.org/3/tutorial/index.html) to
   understand the basics of variable assignment, if and for loops, etc. While
   we are not expecting advanced Python knowledge, everything will go much
   quicker if you are already familiar with the basics.

# Preparing for your lectures and labs

In preparation for your lectures and labs, please ensure that you have your 
Python environment setup properly. You only need to do this once. There are 
alternative approaches to setting up your machine, but the approach outlined 
here is guaranteed to work and is reproducible. Your instructors would be better
able to assist if there are issues in the installation.

1. Download the Python 3.9+ version of [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 
   (recommended) or [Anaconda](https://www.anaconda.com/distribution/) for your
   OS.
2. Follow the official instructions and install Miniconda/Anaconda.
3. Start the terminal (Mac/Linux) or Anaconda Prompt (Windows).
4. Create a virtual environment for NANO181/281:
```bash
conda create --name NANOx81 python=3.9
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
   file from the Google classroom or Github repo and create the environment directly.
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

# Course textbooks

The course is intended to be self-contained and all textbooks are optional.
However, the following are useful to have around:

1. The Elements of Statistical Learning: Data Mining, Inference, and Prediction,
   Second Edition [Amazon](https://www.amazon.com/dp/0387848576/ref=cm_sw_em_r_mt_dp_U_Z8r8DbR3HMYRE),
   or get the [free online version](https://web.stanford.edu/~hastie/Papers/ESLII.pdf).
2. Python Data Science Handbook. Buy from [Amazon](https://www.amazon.com/gp/product/1491912057/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) 
   or get the [free online version](https://jakevdp.github.io/PythonDataScienceHandbook/).
