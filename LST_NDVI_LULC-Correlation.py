#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've uploaded the Excel file and it's named 'your_data.xlsx'
# If your data is in a different file or the columns have different names, adjust accordingly
file_path = '2001-2005.xlsx'
data = pd.read_excel(file_path)

# Convert 'Land_Use_Type' to categorical data type
data['Land_Use_Type'] = pd.Categorical(data['Land_Use_Type'])

# Define your custom color palette
custom_palette = {1: 'green', 2: 'teal', 3: 'cyan', 4: 'yellow', 5: 'red', 6: 'orange', 7: 'blue'}

# Set up the figure and axis
plt.figure(figsize=(10, 8))

# Create a scatter plot with your custom color palette
sns.scatterplot(x='NDVI', y='temperatur', hue='Land_Use_Type', data=data, palette=custom_palette, alpha=0.7)

# Set labels and title
plt.xlabel('Normalized Difference Vegetation Index (NDVI)')
plt.ylabel('Land Surface Temperature (°C)')
plt.title('LST-NDVI Feature Space by Land Use Type')

# Show legend
plt.legend()

# Display the plot
plt.show()


# In[35]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've uploaded the Excel file and it's named 'your_data.xlsx'
# If your data is in a different file or the columns have different names, adjust accordingly
file_path = '2006-2010.xlsx'
data = pd.read_excel(file_path)

# Convert 'Land_Use_Type' to categorical data type
data['Land_Use_Type'] = pd.Categorical(data['Land_Use_Type'])

# Define your custom color palette
custom_palette = {1: 'green', 2: 'teal', 3: 'cyan', 4: 'yellow', 5: 'red', 6: 'orange', 7: 'blue'}

# Set up the figure and axis
plt.figure(figsize=(10, 8))

# Create a scatter plot with your custom color palette
sns.scatterplot(x='NDVI', y='temperatur', hue='Land_Use_Type', data=data, palette=custom_palette, alpha=0.7)

# Set labels and title
plt.xlabel('Normalized Difference Vegetation Index (NDVI)')
plt.ylabel('Land Surface Temperature (°C)')
plt.title('LST-NDVI Feature Space by Land Use Type')

# Show legend
plt.legend()

# Display the plot
plt.show()


# In[32]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've uploaded the Excel file and it's named 'your_data.xlsx'
# If your data is in a different file or the columns have different names, adjust accordingly
file_path = '2011-2015.xlsx'
data = pd.read_excel(file_path)

# Convert 'Land_Use_Type' to categorical data type
data['Land_Use_Type'] = pd.Categorical(data['Land_Use_Type'])

# Define your custom color palette
custom_palette = {1: 'green', 2: 'teal', 3: 'cyan', 4: 'yellow', 5: 'red', 6: 'orange', 7: 'blue'}

# Set up the figure and axis
plt.figure(figsize=(10, 8))

# Create a scatter plot with your custom color palette
sns.scatterplot(x='NDVI', y='temperatur', hue='Land_Use_Type', data=data, palette=custom_palette, alpha=0.7)

# Set labels and title
plt.xlabel('Normalized Difference Vegetation Index (NDVI)')
plt.ylabel('Land Surface Temperature (°C)')
plt.title('LST-NDVI Feature Space by Land Use Type')

# Show legend
plt.legend()

# Display the plot
plt.show()


# In[33]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've uploaded the Excel file and it's named 'your_data.xlsx'
# If your data is in a different file or the columns have different names, adjust accordingly
file_path = '2016-2020.xlsx'
data = pd.read_excel(file_path)

# Convert 'Land_Use_Type' to categorical data type
data['Land_Use_Type'] = pd.Categorical(data['Land_Use_Type'])

# Define your custom color palette
custom_palette = {1: 'green', 2: 'teal', 3: 'cyan', 4: 'yellow', 5: 'red', 6: 'orange', 7: 'blue'}

# Set up the figure and axis
plt.figure(figsize=(10, 8))

# Create a scatter plot with your custom color palette
sns.scatterplot(x='NDVI', y='temperatur', hue='Land_Use_Type', data=data, palette=custom_palette, alpha=0.7)

# Set labels and title
plt.xlabel('Normalized Difference Vegetation Index (NDVI)')
plt.ylabel('Land Surface Temperature (°C)')
plt.title('LST-NDVI Feature Space by Land Use Type')

# Show legend
plt.legend()

# Display the plot
plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've uploaded the Excel file and it's named 'your_data.xlsx'
# If your data is in a different file or the columns have different names, adjust accordingly
file_path = '2001-2005 (1).csv'
data = pd.read_csv(file_path)

# Convert 'Land_Use_Type' to categorical data type
data['Land_Use_Type'] = pd.Categorical(data['Land_Use_Type'])

# Define your custom color palette
custom_palette = {'Forest': 'green', 'Non Forest Vegetation': 'teal', 'Wetlands': 'cyan', 'Croplands': 'yellow', 'Urban & Built up': 'red', 'Barren': 'orange', 'Waterbodies': 'blue'}

# Set up the figure and axis
plt.figure(figsize=(10, 8))

# Create a scatter plot with your custom color palette
sns.scatterplot(x='NDVI', y='temperatur', hue='Land_Use_Type', data=data, palette=custom_palette, alpha=0.7)

# Set labels and title
plt.xlabel('Normalized Difference Vegetation Index (NDVI)')
plt.ylabel('Land Surface Temperature (°C)')
plt.title('LST-NDVI Feature Space by Land Use Type')

# Show legend
plt.legend()

# Display the plot
plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've uploaded the Excel file and it's named 'your_data.xlsx'
# If your data is in a different file or the columns have different names, adjust accordingly
file_path = '2006-2010 (1).csv'
data = pd.read_csv(file_path)

# Convert 'Land_Use_Type' to categorical data type
data['Land_Use_Type'] = pd.Categorical(data['Land_Use_Type'])

# Define your custom color palette
custom_palette = {'Forest': 'green', 'Non Forest Vegetation': 'teal', 'Wetlands': 'cyan', 'Croplands': 'yellow', 'Urban & Built up': 'red', 'Barren': 'orange', 'Waterbodies': 'blue'}

# Set up the figure and axis
plt.figure(figsize=(10, 8))

# Create a scatter plot with your custom color palette
sns.scatterplot(x='NDVI', y='temperatur', hue='Land_Use_Type', data=data, palette=custom_palette, alpha=0.7)

# Set labels and title
plt.xlabel('Normalized Difference Vegetation Index (NDVI)')
plt.ylabel('Land Surface Temperature (°C)')
plt.title('LST-NDVI Feature Space by Land Use Type')

# Show legend
plt.legend()

# Display the plot
plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've uploaded the Excel file and it's named 'your_data.xlsx'
# If your data is in a different file or the columns have different names, adjust accordingly
file_path = '2011-2015.csv'
data = pd.read_csv(file_path)

# Convert 'Land_Use_Type' to categorical data type
data['Land_Use_Type'] = pd.Categorical(data['Land_Use_Type'])

# Define your custom color palette
custom_palette = {'Forest': 'green', 'Non Forest Vegetation': 'teal', 'Wetlands': 'cyan', 'Croplands': 'yellow', 'Urban & Built up': 'red', 'Barren': 'orange', 'Waterbodies': 'blue'}

# Set up the figure and axis
plt.figure(figsize=(10, 8))

# Create a scatter plot with your custom color palette
sns.scatterplot(x='NDVI', y='temperatur', hue='Land_Use_Type', data=data, palette=custom_palette, alpha=0.7)

# Set labels and title
plt.xlabel('Normalized Difference Vegetation Index (NDVI)')
plt.ylabel('Land Surface Temperature (°C)')
plt.title('LST-NDVI Feature Space by Land Use Type')

# Show legend
plt.legend()

# Display the plot
plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've uploaded the Excel file and it's named 'your_data.xlsx'
# If your data is in a different file or the columns have different names, adjust accordingly
file_path = '2016-2020.csv'
data = pd.read_csv(file_path)

# Convert 'Land_Use_Type' to categorical data type
data['Land_Use_Type'] = pd.Categorical(data['Land_Use_Type'])

# Define your custom color palette
custom_palette = {'Forest': 'green', 'Non Forest Vegetation': 'teal', 'Wetlands': 'cyan', 'Croplands': 'yellow', 'Urban & Built up': 'red', 'Barren': 'orange', 'Waterbodies': 'blue'}

# Set up the figure and axis
plt.figure(figsize=(10, 8))

# Create a scatter plot with your custom color palette
sns.scatterplot(x='NDVI', y='temperatur', hue='Land_Use_Type', data=data, palette=custom_palette, alpha=0.7)

# Set labels and title
plt.xlabel('Normalized Difference Vegetation Index (NDVI)')
plt.ylabel('Land Surface Temperature (°C)')
plt.title('LST-NDVI Feature Space by Land Use Type')

# Show legend
plt.legend()

# Display the plot
plt.show()


# In[ ]:




