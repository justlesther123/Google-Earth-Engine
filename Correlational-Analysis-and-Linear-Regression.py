#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# Load data from Excel file
df = pd.read_excel('NDVI_LST 0.xlsx')  # Replace 'your_file.xlsx' with your actual file name

# Assuming you have two columns 'X' and 'Y' for independent and dependent variables
X = df['NDVI2011'].values.reshape(-1, 1)
Y = df['SMMR2011'].values

# Create linear regression model
model = LinearRegression()
model.fit(X, Y)

# Make predictions
Y_pred = model.predict(X)

# Calculate R-squared value
r_squared = r2_score(Y, Y_pred)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(Y, Y_pred))

# Get R value (coefficient of determination)
r_value = model.score(X, Y)

# Plot the data and regression line
plt.scatter(X, Y, label='Actual Data')
plt.plot(X, Y_pred, color='red', label='Regression Line')
plt.xlabel('NDVI')
plt.ylabel('LST')
plt.title('Linear Regression Analysis\nR-squared: {:.2f}, RMSE: {:.2f}, R: {:.2f}'.format(r_squared, rmse, r_value))
plt.legend()
plt.show()


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# Load data from Excel file
df = pd.read_excel('Book14.xlsx')  # Replace 'your_file.xlsx' with your actual file name

# Assuming you have two columns 'X' and 'Y' for independent and dependent variables
X = df['NDVI'].values.reshape(-1, 1)
Y = df['temperatur'].values

# Create linear regression model
model = LinearRegression()
model.fit(X, Y)

# Make predictions
Y_pred = model.predict(X)

# Calculate R-squared value
r_squared = r2_score(Y, Y_pred)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(Y, Y_pred))

# Get R value (coefficient of determination)
r_value = model.score(X, Y)

# Plot the data and regression line
plt.scatter(X, Y, label='temperature')
plt.plot(X, Y_pred, color='red', label='Regression Line')
plt.xlabel('NDVI')
plt.ylabel('LST')
plt.title('Linear Regression Analysis\nR-squared: {:.2f}, RMSE: {:.2f}, R: {:.2f}'.format(r_squared, rmse, r_value))
plt.legend()
plt.show()


# In[ ]:




