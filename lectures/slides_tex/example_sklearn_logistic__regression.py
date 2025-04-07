from __future__ import annotations

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(penalty="none", random_state=0)
model = clf.fit(X, y)
y_pred = model.predict(X)
