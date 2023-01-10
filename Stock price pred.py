import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



# Load the data
data = pd.read_csv("D:/Chandu/n00b/PYTHON/DS/TSLA.csv")

# Extract the relevant columns
X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Close']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict the stock price on the test set
y_pred = model.predict(X_test)

# Print the prediction
print("Predicted Stock Price:", y_pred)
# plt.plot(X_test,y_pred)
plt.plot(X_test, y_test)
plt.show()