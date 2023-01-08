from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset

dataset = pd.read_csv("D:/Chandu/n00b/PYTHON/DS/Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

print(X.size)
print(X)
print(y.size)
# Training Random Forest model on whole dataset

reg = RandomForestRegressor(n_estimators=10, random_state=0)
reg.fit(X, y)

# prediction
Y_pred = reg.predict(X)

# plotting
plt.scatter(X, y, color="red")
plt.plot(X, Y_pred, color="blue")

plt.xlabel("emp Level")
plt.ylabel("Salary")
plt.title("rfr")

plt.show()
