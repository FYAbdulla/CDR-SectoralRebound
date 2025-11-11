#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:59:59 2024

@author: fyabdulla
"""

import pandas as pd

# Load the Excel file
file_path = 'GCAM AR6 CAN CO2.xlsx'
xls = pd.ExcelFile(file_path)

# Load the first sheet into a DataFrame
sheet1 = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

# Create new DataFrames for the new sheets
dac_df = pd.DataFrame(columns=sheet1.columns)
buildings_df = pd.DataFrame(columns=sheet1.columns)
transportation_df = pd.DataFrame(columns=sheet1.columns)
industry_df = pd.DataFrame(columns=sheet1.columns)

# Copy the header row from Sheet1 to each of the new DataFrames
header_row = sheet1.iloc[0].to_frame().T  # Convert row to DataFrame and transpose it
dac_df = pd.concat([dac_df, header_row], ignore_index=True)
buildings_df = pd.concat([buildings_df, header_row], ignore_index=True)
transportation_df = pd.concat([transportation_df, header_row], ignore_index=True)
industry_df = pd.concat([industry_df, header_row], ignore_index=True)

# Filter rows based on the fourth column (Variable) and populate the new sheets
for index, row in sheet1.iterrows():
    if row['Variable'] == "Carbon Sequestration|Direct Air Capture":
        dac_df = pd.concat([dac_df, row.to_frame().T], ignore_index=True)
    elif row['Variable'] == "Emissions|CO2|Energy|Demand|Residential and Commercial":
        buildings_df = pd.concat([buildings_df, row.to_frame().T], ignore_index=True)
    elif row['Variable'] == "Emissions|CO2|Energy|Demand|Transportation":
        transportation_df = pd.concat([transportation_df, row.to_frame().T], ignore_index=True)
    elif row['Variable'] in ["Emissions|CO2|Energy|Demand|Industry", "Emissions|CO2|Industrial Processes"]:
        industry_df = pd.concat([industry_df, row.to_frame().T], ignore_index=True)
        if row['Variable'] == "Emissions|CO2|Industrial Processes":
            # Insert a blank row below for Industrial Processes rows
            blank_row = pd.Series([None] * len(sheet1.columns), index=sheet1.columns)
            industry_df = pd.concat([industry_df, blank_row.to_frame().T], ignore_index=True)

# Create a new Excel writer to save the new sheets
output_file_path = 'GCAM_AR6_CAN_CO2_Modified.xlsx'
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    dac_df.to_excel(writer, sheet_name='DAC', index=False)
    buildings_df.to_excel(writer, sheet_name='Buildings', index=False)
    transportation_df.to_excel(writer, sheet_name='Transportation', index=False)
    industry_df.to_excel(writer, sheet_name='Industry', index=False)

print(f"File saved to {output_file_path}")
