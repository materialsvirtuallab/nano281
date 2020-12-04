from pymatgen.ext.matproj import MPRester
# Change "<APIKEY>" to the API key obtained from MP.
mpr = MPRester("<APIKEY>")
data = mpr.query(criteria={"pretty_formula": "Al2O3"}, 
                 properties=["final_energy", "band_gap"])
print(data)
import pandas as pd
df = pd.DataFrame(data)   # Convert to DataFrame