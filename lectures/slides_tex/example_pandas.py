from __future__ import annotations

import pandas as pd

url = "https://ndownloader.figshare.com/files/13007075"
# Reads in the data as a pandas DataFrame.
data = pd.read_csv(url)

# Extracting a column as a Series.
form_e = data["E_raw (eV)"]

# Summary statistics
data.describe()
