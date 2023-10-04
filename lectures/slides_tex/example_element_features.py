import numpy as np
import pandas as pd
from pymatgen.core import Composition

binaries = pd.read_csv("binary_band_gap.csv")
# We create a column holding the Composition object.
# Note the use of list comprehension in Python.
binaries["composition"] = [Composition(c) for c in binaries["Formula"]]
electronegs = [[el.X for el in c] for c in binaries["composition"]]
# Create the features mean and difference between electronegativities
binaries["mean_X"] = [np.mean(e) for e in electronegs]
binaries["diff_X"] = [max(e) - min(e) for e in electronegs]
# Label metals (band gap of 0. 1e-5 is used as numerical tolerance) as class 0
# Insulators are labelled as class 1.
binaries["class"] = [0 if eg < 1e-5 else 1 for eg in binaries["Eg (eV)"]]
