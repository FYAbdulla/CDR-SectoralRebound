#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:40:21 2024

@author: fyabdulla
"""

import matplotlib.pyplot as plt
import numpy as np

# Hard-coded data for DAC rollout in 2035 and 2040
years = [2035, 2040, 2045, 2050]

# Emissions data (average values) for different sectors under different DAC deployment years
residential_buildings_2035 = [30.282, 28.560, 30.681, 32.105]
commercial_buildings_2035 = [25.496, 23.533, 23.703, 22.766]
light_transport_2035 = [63.406, 50.262, 42.198, 40.622]
medium_heavy_transport_2035 = [55.371, 63.258, 63.370, 64.264]
oil_gas_2035 = [66.050, 54.840, 57.094, 50.870]
industry_2035 = [68.505, 69.225, 78.322, 79.118]
agriculture_waste_2035 = [81.051, 75.883, 73.839, 72.184]
utilities_2035 = [3.562, 6.560, 14.352, 16.727]

residential_buildings_2040 = [30.626, 28.240, 30.267, 32.588]
commercial_buildings_2040 = [25.792, 23.456, 23.651, 23.415]
light_transport_2040 = [54.067, 36.666, 25.855, 23.898]
medium_heavy_transport_2040 = [55.756, 57.357, 56.938, 54.587]
oil_gas_2040 = [67.312, 48.473, 46.752, 42.691]
industry_2040 = [66.025, 60.643, 70.215, 72.772]
agriculture_waste_2040 = [82.422, 76.662, 74.455, 72.602]
utilities_2040 = [3.377, 6.285, 13.445, 18.118]

bar_width = 0.35
bar_positions = np.arange(len(years))

# Plot stacked bar chart for DAC 2035 rollout
plt.figure(figsize=(14, 8))

# Colors as per the request
colors_2035 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
colors_2040 = ['#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7']

plt.bar(bar_positions - bar_width/2, residential_buildings_2035, width=bar_width, color=colors_2035[0], label='Residential Buildings')
plt.bar(bar_positions - bar_width/2, commercial_buildings_2035, width=bar_width, bottom=np.array(residential_buildings_2035), color=colors_2035[1], label='Commercial Buildings')
plt.bar(bar_positions - bar_width/2, light_transport_2035, width=bar_width, bottom=np.array(residential_buildings_2035) + np.array(commercial_buildings_2035), color=colors_2035[2], label='Light Transport')
plt.bar(bar_positions - bar_width/2, medium_heavy_transport_2035, width=bar_width, bottom=np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035), color=colors_2035[3], label='Med/Hvy Transport')
plt.bar(bar_positions - bar_width/2, oil_gas_2035, width=bar_width, bottom=np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035), color=colors_2035[4], label='Oil & Gas')
plt.bar(bar_positions - bar_width/2, industry_2035, width=bar_width, bottom=np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035) + np.array(oil_gas_2035), color=colors_2035[5], label='Industry')
plt.bar(bar_positions - bar_width/2, agriculture_waste_2035, width=bar_width, bottom=np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035) + np.array(oil_gas_2035) + np.array(industry_2035), color=colors_2035[6], label='Agriculture & Waste')
plt.bar(bar_positions - bar_width/2, utilities_2035, width=bar_width, bottom=np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035) + np.array(oil_gas_2035) + np.array(industry_2035) + np.array(agriculture_waste_2035), color=colors_2035[7], label='Utilities')

# Plot stacked bar chart for DAC 2040 rollout
plt.bar(bar_positions + bar_width/2, residential_buildings_2040, width=bar_width, color=colors_2040[0])
plt.bar(bar_positions + bar_width/2, commercial_buildings_2040, width=bar_width, bottom=np.array(residential_buildings_2040), color=colors_2040[1])
plt.bar(bar_positions + bar_width/2, light_transport_2040, width=bar_width, bottom=np.array(residential_buildings_2040) + np.array(commercial_buildings_2040), color=colors_2040[2])
plt.bar(bar_positions + bar_width/2, medium_heavy_transport_2040, width=bar_width, bottom=np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040), color=colors_2040[3])
plt.bar(bar_positions + bar_width/2, oil_gas_2040, width=bar_width, bottom=np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040), color=colors_2040[4])
plt.bar(bar_positions + bar_width/2, industry_2040, width=bar_width, bottom=np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040) + np.array(oil_gas_2040), color=colors_2040[5])
plt.bar(bar_positions + bar_width/2, agriculture_waste_2040, width=bar_width, bottom=np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040) + np.array(oil_gas_2040) + np.array(industry_2040), color=colors_2040[6])
plt.bar(bar_positions + bar_width/2, utilities_2040, width=bar_width, bottom=np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040) + np.array(oil_gas_2040) + np.array(industry_2040) + np.array(agriculture_waste_2040), color=colors_2040[7])

# Customizing the x-axis with labels and captions
plt.xticks(bar_positions, [f"{year}" for year in years], y=-0.03)  # Move year labels down

# Adding captions for 2035 Rollout and 2040 Rollout above the year labels
for i, pos in enumerate(bar_positions):
    plt.text(pos - bar_width/2, -10, '2035 Rollout', ha='center', va='center', fontsize=10, color='black')
    plt.text(pos + bar_width/2, -10, '2040 Rollout', ha='center', va='center', fontsize=10, color='black')

# Remove the x-axis label
plt.xlabel('')

# Move the legend to the right of the chart, listing only one set of entries
plt.legend(title='Sector', bbox_to_anchor=(1.05, 1), loc='upper left', labels=[
    'Residential Buildings', 'Commercial Buildings', 'Light Transport', 'Med/Hvy Transport', 
    'Oil & Gas', 'Industry', 'Agriculture & Waste', 'Utilities'
])

# Remove vertical gridlines
plt.grid(axis='x')  # Only keep horizontal gridlines

plt.ylabel('Emissions (MT CO2e)')
plt.title('Sectoral Emissions by DAC Rollout Year')
plt.tight_layout()
plt.show()


