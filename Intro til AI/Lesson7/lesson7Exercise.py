import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

data = pd.read_csv("CO2data.csv")

X = data[["Weight", "Volume"]].values
y = data[["CO2"]].values

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")


ax.scatter(X[:, 1], y, c="b", marker="o")

ax.set_xlabel("Weight")
ax.set_ylabel("Volume")
ax.set_zlabel("CO2")

plt.show()

lin_reg =  LinearRegression()
weight = LinearRegression().fit(X[:, 0].reshape(-1,1), y)
y_pred = weight.predict(X[:, 0].reshape(-1, 1))
mse = mean_squared_error(y, y_pred)
print("Weight model MSE: ", mse)

volume = LinearRegression().fit(X[:,1].reshape(-1,1), y)
y_pred = volume.predict(X[:, 1].reshape(-1, 1))
mse = mean_squared_error(y, y_pred)
print("Volume model MSE: ", mse)

lin_reg = LinearRegression().fit(X, y)
y_pred = lin_reg.predict(X)
mse = mean_squared_error(y, y_pred)
print("Full model MSE: ", mse)

y_pred = lin_reg.predict([[2300, 1300]])
print(y_pred)

# Visualize the regression plane
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of actual data
ax.scatter(X[:, 0], X[:, 1], y, c='b', marker='o', label='Actual Data')

# Create a mesh grid for the plane
x_grid, y_grid = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), 20),
                             np.linspace(X[:, 1].min(), X[:, 1].max(), 20))

z_grid = lin_reg.intercept_ + lin_reg.coef_[0] * x_grid + lin_reg.coef_[1] * y_grid

# Plot the regression plane
ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis', alpha=0.5)

# Set labels for axes and a title
ax.set_xlabel('Weight')
ax.set_ylabel('Volume')
ax.set_zlabel('CO2')

# Show the plot
plt.show()