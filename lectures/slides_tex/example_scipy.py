from __future__ import annotations

from scipy import stats  # Statistics package

dist = stats.norm(0, 1)  # Gaussian distribution
print(dist.cdf(1.96))
# Result: 0.9750021048517795
from scipy import constants  # Physical constants

print(constants.e)
# Result: 1.6021766208e-19
