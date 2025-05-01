#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:17:41 2024

@author: fyabdulla
"""

import matplotlib.pyplot as plt
import numpy as np

# Input the data manually
years = [2035, 2040, 2045, 2050]

Rollout_2035_min = [0.00000194, 52.78659127, 162.2808579, 262.451609]
Rollout_2035_max = [33.42511432, 148.6889369, 292.4924718, 407.2197685]

Rollout_2040_min = [0, 41.676, 143.009, 236.228]
Rollout_2040_max = [0, 70.433, 200.950, 334.087]

# Define categories and their colors for consistent plotting
categories = [
    ('2035 DAC Rollout', Rollout_2035_min, Rollout_2035_max, 'blue'),
    ('2040 DAC Rollout', Rollout_2040_min, Rollout_2040_max, 'orange'),
]

# Plot each category
plt.figure(figsize=(12, 8))

for category, min_values, max_values, color in categories:
    min_values = np.array(min_values, dtype=np.float64)
    max_values = np.array(max_values, dtype=np.float64)
    
    plt.plot(years, min_values, label=f'{category}', linestyle='-', color=color)
    plt.plot(years, max_values, label=None, linestyle='-', color=color)
    plt.fill_between(years, min_values, max_values, color=color, alpha=0.2)

# Set x-ticks to only show specific years
plt.xticks([2035, 2040, 2045, 2050])

# Add labels and title
plt.xlabel('Year', fontsize=14)
plt.ylabel('Annual DAC Negative Emissions (MT CO2e)', fontsize=14)
plt.title('DAC Deployment Ranges Based on Time of Rollout', fontsize=14)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=2)

# Display the plot
plt.show()

