from __future__ import annotations

model = Model(**params)  # Init a model with parameters.
model.get_params()  # Get model parameters.
model.set_params(**params)  # Set model parameters
model.fit(X, y)  # Fit the model with a dataset
model.score(X, y)  # Provides the score for the dataset.
model.predict(X)  # Make a prediction using fitted model.
