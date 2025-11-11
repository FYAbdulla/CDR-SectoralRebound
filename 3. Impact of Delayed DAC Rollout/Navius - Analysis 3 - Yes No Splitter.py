#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:56:24 2024

@author: fyabdulla
"""

import pandas as pd

# Load the Excel file and the 'National' sheet
file_path = 'Navius - Analysis 3.xlsx'
df = pd.read_excel(file_path, sheet_name='National')

# Remove rows with 'legislated' in the 'Policy' column
df = df[df['Policy'] != 'legislated']

# Split the DataFrame into two based on 'DAC Availability'
df_yes = df[df['DAC Availability'] == 'yes'].copy()
df_no = df[df['DAC Availability'] == 'no'].copy()

# Create lists to hold the final rows for the new sheets
final_yes_rows = []
final_no_rows = []

# Iterate over each row in the 'yes' DataFrame
for _, yes_row in df_yes.iterrows():
    # Find the matching row in the 'no' DataFrame
    matching_no_rows = df_no[
        (df_no['Year'] == yes_row['Year']) &
        (df_no['Policy'] == yes_row['Policy']) &
        (df_no['Solar Wind Batteries Cost'] == yes_row['Solar Wind Batteries Cost']) &
        (df_no['CCS Cost'] == yes_row['CCS Cost']) &
        (df_no['Hydrogen Cost'] == yes_row['Hydrogen Cost']) &
        (df_no['Oil Price'] == yes_row['Oil Price']) &
        (df_no['Land Use Offsets'] == yes_row['Land Use Offsets'])
    ]
    
    if not matching_no_rows.empty:
        # Add the 'yes' row to the final list
        final_yes_rows.append(yes_row)
        
        # Add the corresponding 'no' row to the final list
        final_no_rows.append(matching_no_rows.iloc[0])
        
        # Remove the matched 'no' row from the original 'no' DataFrame to avoid duplication
        df_no = df_no.drop(matching_no_rows.index[0])

# Convert the final lists into DataFrames
final_yes_df = pd.DataFrame(final_yes_rows)
final_no_df = pd.DataFrame(final_no_rows)

# Create a new Excel file with two sheets: 'DAC YES' and 'DAC NO'
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    final_yes_df.to_excel(writer, sheet_name='DAC YES', index=False)
    final_no_df.to_excel(writer, sheet_name='DAC NO', index=False)

print("The sheets 'DAC YES' and 'DAC NO' have been created successfully.")
