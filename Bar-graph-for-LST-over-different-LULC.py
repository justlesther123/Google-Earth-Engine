#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    'Year': [2001, 2010, 2020],
    'Forest': [25.5, 26.3, 26.1],
    'Non-forest Vegetation': [29.1, 31.2, 30.4],
    'Wetlands': [27.2, 28.2, 28.2],
    'Croplands': [31.4, 33.2, 32.9 ],
    'Urban/Built-up Area': [32.7, 34.6, 34.6], 
    'Barren lands': [27.9, 30.5, 31.2], 
    'Waterbodies': [26.9, 27.5, 27.6],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Plotting the grouped bar graph with increased space
bar_width = 0.15  # Adjust the width of bars as needed
space_between_bars = 0.4  # Adjust the space between bars as needed
bar_positions = np.arange(len(df['Year']))


plt.figure(figsize=(25, 8))  # Adjust the figure size as needed

bars = []

bars.append (plt.bar(bar_positions - 3*bar_width, df['Forest'], width=bar_width, label='Forest', color='green'))
bars.append (plt.bar(bar_positions - 2*bar_width, df['Non-forest Vegetation'], width=bar_width, label='Non-forest Vegetation', color='teal'))
bars.append (plt.bar(bar_positions - bar_width, df['Wetlands'], width=bar_width, label='Wetlands', color='cyan'))
bars.append (plt.bar(bar_positions, df['Croplands'], width=bar_width, label='Croplands', color='yellow'))
bars.append (plt.bar(bar_positions + bar_width, df['Urban/Built-up Area'], width=bar_width, label='Urban/Built-up Area', color='red'))
bars.append (plt.bar(bar_positions + 2*bar_width, df['Barren lands'], width=bar_width, label='Barren lands', color='orange'))
bars.append (plt.bar(bar_positions + 3*bar_width, df['Waterbodies'], width=bar_width, label='Waterbodies', color='blue'))

# Add temperature values on top of the bars
for bar in bars:
    for b in bar:
        plt.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.3,
                 '{:.1f}'.format(b.get_height()), ha='center', fontsize=12)
        
# Customize the plot
plt.xlabel('Year', fontsize=16)
plt.ylabel('Land Surface Temperature (Celsius)', fontsize=16)
plt.title('Land Surface Temperature over Different Land Uses and Land Covers', fontsize=18)
plt.xticks(bar_positions, df['Year'])
plt.legend()
plt.grid(True)


# Show the plot
plt.show()


# In[ ]:




