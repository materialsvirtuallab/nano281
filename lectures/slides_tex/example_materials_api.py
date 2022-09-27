from pymatgen.ext.matproj import MPRester

# Change "<APIKEY>" to the API key obtained from MP.
with MPRester("<APIKEY>") as mpr:
    data = mpr.summary.search(
        formula=["Fe2O3"],
        fields=["formula_pretty", "formation_energy_per_atom", "band_gap"],
    )

print(data)
import pandas as pd

df = pd.DataFrame([d.dict() for d in data])  # Convert to DataFrame
