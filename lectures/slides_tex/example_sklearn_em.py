from __future__ import annotations

from sklearn.mixture import GaussianMixture

estimator = GaussianMixture(n_components=n_classes, covariance_type="spherical", max_iter=20, random_state=0)
estimator.means_init = np.array([x_train[y_train == i].mean(axis=0) for i in range(n_classes)])
estimator.fit(x_train)
