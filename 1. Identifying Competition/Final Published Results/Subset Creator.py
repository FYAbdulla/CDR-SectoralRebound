# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:58:17 2024

@author: Feras Abdulla
"""

import pandas as pd

# Read the Excel file
df = pd.read_excel("Universe1.xlsx")

# Define the columns to be selected
columns_to_select = ['year', 'policy', 'swb', 'ccs', 'hyd', 'oil', 'lul']

# Split the data based on the 'dac' column
yes_data = df[df['dac'] == 'yes'][columns_to_select + ['dac', 'agriculture & waste', 'commercial buildings', 'industry', 'light-duty transport', 'medium and heavy transport', 'other transport', 'oil and gas', 'land use and forestry', 'residential buildings', 'utilities', 'direct air capture']]
no_data = df[df['dac'] == 'no'][columns_to_select + ['dac', 'agriculture & waste', 'commercial buildings', 'industry', 'light-duty transport', 'medium and heavy transport', 'other transport', 'oil and gas', 'land use and forestry', 'residential buildings', 'utilities', 'direct air capture']]

# Sort the dataframes based on columns x1 to x6
yes_data = yes_data.sort_values(by=columns_to_select)
no_data = no_data.sort_values(by=columns_to_select)

# Save the divided data to new Excel files or process them as needed
yes_data.to_excel("yes_data.xlsx", index=False)
no_data.to_excel("no_data.xlsx", index=False)