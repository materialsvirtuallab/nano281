from io import StringIO
import pandas as pd
import requests

# Get the raw text of the data directly from the figshare url.
url = "https://ndownloader.figshare.com/files/13007075"
raw = requests.get(url).text
# Then reads in the data as a pandas DataFrame.
data = pd.read_csv(StringIO(raw))

# Extracting a column as a Series.
form_e = data['E_raw (eV)']

# Summary statistics
data.describe()