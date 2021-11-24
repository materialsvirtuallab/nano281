# Introduction

Welcome to the final lab of NANO281 - Data Science in Materials Science. Unlike previous labs, this lab is deliberately more open-ended. The lack of instructions is deliberate to allow students to exercise their creativity in finding the best solution.

# Getting started

Same as the previous lab, you need to set up your computer environment before the lab. 

1. Activate your nano281 virtual environment.

```bash
conda activate nano281
```
2. Start a Jupyter notebook.

```bash
jupyter notebook
```
3. Create a Python 3 notebook and rename it `nano281-lab3-<first_name>-<last_name>`.

# Assessment criteria

Try to complete all questions, doing everything in your Jupyter notebook. Make generous use of code cells, text cells, etc.  and write your notebook as though it is a lab report but with Python code incorporated. The easier you make it for your instructors to find the answers, the better.

At the end of the lab, please submit the `nano281-lab2-<first_name>-<last_name>.ipynb` file (it should be in whatever directory you started your jupyter notebook application in) via Canvas.

Our assessment criteria:

- Model performance: 30%
- Materials Science Insights: 30%
- Data Science Technique: 30%
- Programming Style: 10%


# Lab

Now that we are at the Final Lab, hints will be minimal. In any case, the problem itself is an **open-ended** one where the instructors have no clear idea what the best final solution would be. It is expected that your ML models are properly trained using best practices, your notebooks are clearly annotated and your code is Pythonic. All these will be accounted for in your final score.

## Problem

The dielectric constant is a fundamental property of a material. The Materials Project today already contains around 7800 dielectric constants. The dataset you will be provided contains the following:

- `material_id` A unique identifier for each material in the Materials Project database
- `dielectric_poly_total` The computed polycrystalline total dielectric constant.

For other information, such as structure and composition, you will need to query using `material_id` from the Materials Project.

Build the best machine learning models you can to predict the total dielectric constants from either compositional features or a combination of compositional and structural features. You may obtain compositional features by constructing them from attributes available in the `Element` class in pymatgen (see [documentation here](https://pymatgen.org/pymatgen.core.periodic_table.html?highlight=element#pymatgen.core.periodic_table.Element)), similar to what you have done in lab 2. You can choose whatever reasonable attributes and transformation of attributes you wish. You may also use structural information, but it will be up to you to figure out the best structural representation. You will need to look at the `sample_submission.csv` to see what kind of files you should be submitting. Your results will be on the leaderboard of the Kaggle competition. 

Some very broad hints:
1. Think carefully about the underlying science of dielectric constants. Choose your features and transformations like a materials scientist, not a data scientist.
2. Since this is the final lab, I am expecting well-written code with clear documentation on every step. Explain your thinking behind every single thing you do. Use Jupyter's markdown cells to present your thought processes. Note that I can only give you points only if I am able to understand your code and thought processes. Raw performance on accuracy is not going to be sufficient.

Lab3 is hosted on Kaggle. Please use the private link posted in Canvas to access the competition.
