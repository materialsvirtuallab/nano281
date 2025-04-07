from __future__ import annotations

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(x)
x_pca = pca.transform(x)
print(pca.explained_variance_)

# Linear regression using PCA components
from sklearn import linear_model
from sklearn.model_selection import KFold, cross_val_predict

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
mlr = linear_model.LinearRegression()
yhat_mlr = cross_val_predict(mlr, x_pca[:, 0:2], y, cv=kfold)
