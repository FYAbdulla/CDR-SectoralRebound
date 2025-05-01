#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:07:30 2024

@author: fyabdulla
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# New data provided
data = {
    "SSP1-1p9": [-0.132, -0.321, -0.257, 0.821],
    "SSP1-2p6": [-0.962, -0.945, -0.933, 0.899],
    "SSP2-2p6": [-0.517, -0.811, -0.900, -0.971],
    "SSP4-1p9": [0.056, -0.325, -0.271, -0.229],
    "SSP4-2p6": [0.870, 0.870, 0.834, -0.532],
    "SSP5-2p6": [-0.233, -0.819, -0.894, -0.816]
}

# Sector names
sectors = ["Industry", "Commercial", "Residential", "Transportation"]

# Create DataFrame
df = pd.DataFrame(data, index=sectors)

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap='coolwarm', center=0, linewidths=.5)
plt.title('Percentage Correlation Coefficients between DAC Deployment and Sectoral Emission Rates')
plt.xlabel('Scenarios')
plt.ylabel('Sectors')
plt.show()
