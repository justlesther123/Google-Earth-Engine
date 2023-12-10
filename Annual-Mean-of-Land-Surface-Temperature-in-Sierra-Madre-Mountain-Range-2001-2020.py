#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_name = 'Annual_Mean_LST_2001_2020.csv'
data = pd.read_csv(file_name)

# Assuming the 'Month' column represents the months
months = data['Date']

# Extract unique years from the dataset
unique_years = data.columns[1:]  # Assuming the first column is 'Month'

# Specify the years you want to plot
years_to_plot = [2001, 2002, 2003, 2004, 2005]

# Plotting the time series for every year with years on the x-axis
plt.figure(figsize=(12, 6))

for year in unique_years:
    plt.plot(months, data[year], label=year)

plt.xlabel('Year')
plt.ylabel('LST (°C)')
plt.title('Annual Land Surface Temperature in Sierra Madre Mountain Range Over Time (2001-2020)')


# Set ticks at every data point
plt.xticks(months, rotation=45, ha='right')  # Adjust rotation and alignment as needed
plt.tight_layout()  # Ensure proper layout
plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_name = 'for time series.csv'
data = pd.read_csv(file_name)

# Assuming the 'Month' column represents the months
months = data['Year']

# Extract unique years from the dataset
unique_years = data.columns[1:]  # Assuming the first column is 'Month'

# Specify the years you want to plot
years_to_plot = [2005, 2010, 2015, 2020]


# Plotting the time series for every year with years on the x-axis
plt.figure(figsize=(12, 6))

for year in unique_years:
    plt.plot(months, data[year], label=year)

plt.xlabel('Year')
plt.ylabel('LST (°C)')
plt.title('Annual Land Surface Temperature in Sierra Madre Mountain Range Over Time (2001-2020)')




# In[ ]:




