# -*- coding: utf-8 -*-
"""code2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17VsJjj1PHCDmhTnDV29pvchpr52Vf_e5
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(df.columns)

average_price_by_year = df.groupby('Year')['Price'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='Price', data=average_price_by_year)
plt.title('Average Price of Cars by Year')
plt.xlabel('Year')
plt.ylabel('Average Price (in Lakhs)')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=30, kde=True)  # Assuming 'Price' is in Lakhs
plt.title('Distribution of Car Prices')
plt.xlabel('Price (in Lakhs)')
plt.ylabel('Frequency')
plt.show()

numerical_columns = df[['Year', 'Kilometers_Driven', 'Price']]

# Step 2: Create a pairplot
sns.pairplot(numerical_columns)
plt.suptitle('Pairplot of Numerical Features', y=1.02)  # Adjust title position
plt.show()