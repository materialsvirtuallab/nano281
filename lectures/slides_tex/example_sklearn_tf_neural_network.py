from __future__ import annotations

from sklearn.neural_network import MLPRegressor

nn = MLPRegressor(hidden_layer_sizes=(5, 3), alpha=1e-4, max_iter=200, learning_rate_init=0.01)
nn.fit(x, y_reg)

# Equivalent Tensorflow 2.0
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

x_in = Input(shape=(x.shape[1],))
x_h1 = Dense(5, activation="relu")(x_in)
x_h2 = Dense(3, activation="relu")(x_h1)
x_out = Dense(1)(x_h2)
model = Model(inputs=x_in, outputs=x_out)
opt = Adam(learning_rate=0.01)
model.compile(optimizer=opt, loss="mse")
model.fit(x, y_reg, epochs=200, batch_size=200)
