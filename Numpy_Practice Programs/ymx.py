import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data 1: Straight line data (with some noise)
x1 = np.linspace(0, 10, 30).reshape(-1, 1)
y1 = 2 * x1 + 3 + np.random.randn(30, 1) * 2  # y = 2x + 3 + noise

# Fit linear regression model
model1 = LinearRegression()
model1.fit(x1, y1)
y1_pred = model1.predict(x1)

# Data 2: Curved data (parabola)
x2 = np.linspace(-5, 5, 50).reshape(-1, 1)
y2 = x2**2 + np.random.randn(50, 1) * 3  # y = x^2 + noise

# Fit linear regression model
model2 = LinearRegression()
model2.fit(x2, y2)
y2_pred = model2.predict(x2)

# Plot
plt.figure(figsize=(12, 5))

# Plot 1: Straight line data
plt.subplot(1, 2, 1)
plt.scatter(x1, y1, color="blue", label="Data points")
plt.plot(x1, y1_pred, color="red", linewidth=2, label="Fitted Line")
plt.title("Case 1: Data ~ Straight line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Plot 2: Curved data
plt.subplot(1, 2, 2)
plt.scatter(x2, y2, color="blue", label="Data points")
plt.plot(x2, y2_pred, color="red", linewidth=2, label="Fitted Line")
plt.title("Case 2: Data ~ Curve (x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()
