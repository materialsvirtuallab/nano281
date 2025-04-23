"""Some utility functions for the lecture notebooks."""
from __future__ import annotations

import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def train_fit_plot_model(model, x, y, split=0.1, random_state=42):
    """
    Trains a machine learning model, evaluates it using both training and test data splits,
    and generates a scatter plot showing predicted vs. actual values of the target variable.
    The plot also includes metrics like R² and mean squared error (MSE) for quick evaluation
    of model performance on train and test datasets.

    :param model: A scikit-learn style machine learning model with fit, predict, and score methods.
    :type model: Any
    :param x: Feature dataset to be used for training and testing.
    :type x: array-like
    :param y: Target variable corresponding to the feature dataset.
    :type y: array-like
    :param split: Fraction of the dataset to be used for testing. Default is 0.1 (10%).
    :type split: float, optional
    :param random_state: Seed for the random number generator used for dataset splitting. Default is 42.
    :type random_state: int, optional
    :return: Axes object containing the generated scatter plot for predicted vs. actual values.
    :rtype: matplotlib.axes._axes.Axes
    """
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=split, random_state=random_state)
    model.fit(X_train, y_train)
    yhat_train = model.predict(X_train)
    yhat_test = model.predict(X_test)

    r2_train = model.score(X_train, y_train)
    r2_test = model.score(X_test, y_test)

    mse_train = mean_squared_error(yhat_train, y_train)
    mse_test = mean_squared_error(yhat_test, y_test)
    f, ax = plt.subplots(figsize=(8, 8))
    plt.plot(y_train, yhat_train, "o", label=f"Train: $R^2$ = {r2_train:.3f}, MSE={mse_train:.1f}")
    plt.plot(y_test, yhat_test, "o", label=f"Test: $R^2$ = {r2_test:.3f}, MSE={mse_test:.1f}")
    plt.ylabel(r"$K_{predicted}$ (GPa)")
    plt.xlabel(r"$K$ (GPa)")
    plt.legend()
    plt.xlim([0, 410])
    plt.ylim([0, 410])
    plt.plot([0, 410], [0, 410], "k--")
    return ax
