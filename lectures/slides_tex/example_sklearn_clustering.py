# Reading images using matplotlib
from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib import image

# load image as numpy array.
data = image.imread("example.png")
# Display image
plt.imshow(data)

from sklearn.cluster import DBSCAN

clustering = KMeans(k).fit(X)
print(clustering.labels_)
clustering = DBSCAN(eps=3, min_samples=2).fit(X)
print(clustering.labels_)
