# Reading images using matplotlib
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
# load image as numpy array.
data = image.imread('example.png')
# Display image
plt.imshow(data)

from sklearn.cluster import kmeans, DBSCAN
clustering = KMeans(k).fit(X)
print(clustering.labels_)
clustering = DBSCAN(eps=3, min_samples=2).fit(X)
print(clustering.labels_)