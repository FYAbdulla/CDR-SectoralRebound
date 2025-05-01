#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:06:53 2024

@author: fyabdulla
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data provided
data = {
    "SSP1-1p9": [-0.899, -0.844, -0.858, 0.774],
    "SSP1-2p6": [-0.778, -0.799, -0.891, 0.521],
    "SSP2-2p6": [-0.429, -0.301, -0.122, 0.706],
    "SSP4-1p9": [-0.990, -0.892, -0.892, 0.717],
    "SSP4-2p6": [-0.923, -0.885, -0.862, 0.812],
    "SSP5-2p6": [-0.779, -0.495, -0.363, 0.783]
}

# Sector names
sectors = ["Industry", "Commercial", "Residential", "Transportation"]

# Create DataFrame
df = pd.DataFrame(data, index=sectors)

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap='coolwarm', center=0, linewidths=.5)
plt.title('Absolute Correlation Coefficients between DAC Deployment and Sectoral Emissions')
plt.xlabel('Scenarios')
plt.ylabel('Sectors')
plt.show()
