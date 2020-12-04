from sklearn.discriminant_analysis import LinearDiscriminantAnalysis,
    QuadraticDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
X = binaries[["mean_X", "diff_X"]]
y = binaries["class"]
model = lda.fit(X, y)
y_pred = model.predict(X)

qda = QuadraticDiscriminantAnalysis(store_covariance=True)
y_pred = qda.fit(X, y).predict(X)
\end{minted}