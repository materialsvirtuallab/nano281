# Introduction

Welcome to the final lab of NANO281 - Data Science in Materials Science. Unlike previous labs, this lab will be based on an **open** problem in materials science: how do we determine crystal structure from a diffraction pattern, specifically an X-ray diffraction pattern?

![XRD](https://github.com/materialsvirtuallab/nano281/blob/master/labs/lab3/xrd.png?raw=true)

**XRD pattern of Sr2LiAlO4, the first known phase in the Sr-Li-Al-O system.[3]**

Calculating the XRD pattern from a known crystal structure is relatively easy. The peak positions are governed by Bragg's law, and the intensities of the peaks are given by the types of atoms present as well as the symmetry of the crystal (see lecture notes from NANO106 or any crystallography text book). However, the inverse problem of predicting the crystal structure (lattice system, space group and atomic species and coordinates) is non-trivial. Typically, this is done via Rietveld refinement by matching a measured XRD pattern to a database of reference XRD patterns (using a least squares approach).

In this lab, we want to determine if we can bypass the matching process altogether using machine learning - can we classify an XRD pattern into one of the 14 3D Bravais lattices? Recent works that have attempted such inverse mappings, e.g., local environment from K-edge XANES[1] and Bravais lattice from electron diffraction,[2] provide optimism that this should be achievable.

# Getting started

Same as previous lab, you need to set up your computer environment before the lab. 

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

Try to complete all questions, doing everything in your Jupyter notebook. Make generous use of code cells, text cells, etc. and write your notebook as though it is a lab report but with Python code incorporated. The easier you make it for your instructors to find the answers, the better.

At the end of the lab, please submit the `nano281-lab2-<first_name>-<last_name>.ipynb` file (it should be in whatever directory you started your jupyter notebook application in) via Google classroom.

Our assessment criteria:

- Model performance: 30%
- Materials Science Insights: 30%
- Data Science Technique: 30%
- Programming Style: 10%


# Lab

Now that we are at the Final Lab, hints will be minimal. In any case, the problem itself is an **open-ended** one where the instructors have no clear idea what the best final solution would be (though we can make intelligent guesses). It is expected that your ML models are properly trained using best practices, your notebooks are clearly annotated and your code is Pythonic. All these will be accounted for in your final score.

## Data

We will be using *computed* XRD patterns of crystal structures that have been obtained from the [Crystallography Open Database](http://www.crystallography.net/cod/). The reason we are using computed XRD patterns is to avoid having to deal with background and noise, all of which needs to be handled for experimentally measured XRD patterns. This is therefore a clean dataset that suffices to demonstrate that the problem is in principle solvable via machine learning. We can adapt the technique to work on experimentally measured XRD patterns subsequently. The XRD patterns were computed using [pymatgen's](http://pymatgen.org) XRDCalculator, with a Gaussian smearing of 0.2 eV applied and sampling carried out at 0.5 degree intervals of 2 theta from 0.5 to 90 degrees.


- cod_id: COD id
- formula: Formula
- spacegroup_number: International Space Group Number. This is an integer ranging from 1-230.
- bravais_lattice: Bravais lattice. This is one of 14 string values (aP, mP, mS, oP, oS, oI, oF, tP, tI, cP, cI, cF, hP, hR). The first letter denotes the crystal system (a: anortic or triclinic; m: monoclinic; o: orthorhombic; t: tetragonal; c: cubic; h: hexagonal) and the second letter denotes the centering (P: primitive; S: side centered (a collective for the more commonly used A, B or C centered); I: body centered; F: face centered; R: rhombohedral; H: hexagonal).
- 180 columns of intensity values at 2theta ranging from 0.5 to 90 degrees (inclusive) in 0.5 degree intervals.

Lab3 is hosted on Kaggle, please visit using this [link])(https://www.kaggle.com/t/2b2a24d3729b4ec2b226904039b5ea78).

![3D_bravais_lattices](https://github.com/materialsvirtuallab/nano281/blob/master/labs/lab3/bravais_lattices.png?raw=true)

**The 14 3D bravais lattices.**

## Q1 - Predicting bravais lattice from XRD

Develop a machine learning (ML) model to classify an XRD pattern into one of the 14 Bravais lattices. Experiment with any or all of the ML models that you have learnt so far in the course, and play around with various parameters. Given the size of the data, it is recommended that you sample only 10000 data points and use that to experiment with different models first, before trying to use the full data set to do a proper series of fits. Show all parameter optimizations carried out, e.g., grid search of relevant parameters. You should demonstrate the usage of at least two types of ML model (linear, trees, neural networks, etc.)

Please save your *three best models* using:

```python
import pickle
with open('<First_name>_<Last_name>_<description of model, e.g., linear, tree, etc.>.pkl') as f:
    pickle.dump(model, f)
```

Generate a csv with your best model with two columns:

- id: dummy id used in the test file
- bravais\_lattice: Predicted Bravais Lattice from your model.

Report your classification accuracy.

In your notebook, discuss the results you have obtained, offering materials science based interpretations of how your model is achieving the performance claimed. Compare the results you have obtained with what would have been achieved based on random guessing. Is the ML model doing anything useful?

## Q2 - Optional Hard Challenge Problem

Repeat Q1, but instead of classifying the XRD patterns based on the 14 Bravais lattices, predict the correct space group classification.

# References

[1]: Zheng, C.; Chen, C.; Chen, Y.; Ong, S. P. Random Forest Models for Accurate Identification of Coordination Environments from X-Ray Absorption Near-Edge Structure. arXiv:1911.01358 [cond-mat] 2019.

[2]: Kaufmann, K.; Zhu, C.; Rosengarten, A. S.; Maryanovsky, D.; Harrington, T. J.; Marin, E.; Vecchio, K. S. Crystal Symmetry Determination in Electron Diffraction Using Machine Learning. Science 2020, 367 (6477), 564–568. https://doi.org/10.1126/science.aay3062.

[3]: Wang, Z.; Ha, J.; Kim, Y. H.; Im, W. B.; McKittrick, J.; Ong, S. P. Mining Unexplored Chemistries for Phosphors for High-Color-Quality White-Light-Emitting Diodes. Joule 2018, 2 (5), 914–926. https://doi.org/10.1016/j.joule.2018.01.015.


