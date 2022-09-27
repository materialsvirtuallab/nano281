import matplotlib.pyplot as plt

# Plot two variables x and y with 'x' as markers and solid lines.
plt.plot(x, y, "x-")
# Use circles as markers and dashed lines instead.
plt.plot(x, y, "o--")

import seaborn as sns

# Plot the distribution of x.
sns.distplot(x)
# Scatter plot using columns from DataFrame
sns.scatterplot(x="Melting point", y="Modulus", data=materials)
