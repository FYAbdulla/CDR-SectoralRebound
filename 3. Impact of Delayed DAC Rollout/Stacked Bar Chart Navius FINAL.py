#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:50:16 2024

@author: fyabdulla
"""

import matplotlib.pyplot as plt
import numpy as np

# Hard-coded data for DAC rollout in 2035 and 2040
years = [2035, 2040, 2045, 2050]

# Emissions data (average values) for different sectors under different DAC deployment years
#residential_buildings_2035 = [30.282, 28.560, 30.681, 32.105]
#commercial_buildings_2035 = [25.496, 23.533, 23.703, 22.766]
light_transport_2035 = [63.406, 50.262, 42.198, 40.622]
medium_heavy_transport_2035 = [55.371, 63.258, 63.370, 64.264]
#other_transport_2035 = [14.41, 15.65, 17.51, 18.88]
oil_gas_2035 = [66.050, 54.840, 57.094, 50.870]
industry_2035 = [68.505, 69.225, 78.322, 79.118]
#agriculture_waste_2035 = [81.051, 75.883, 73.839, 72.184]
#utilities_2035 = [3.562, 6.560, 14.352, 16.727]

#residential_buildings_2040 = [30.626, 28.240, 30.267, 32.588]
#commercial_buildings_2040 = [25.792, 23.456, 23.651, 23.415]
light_transport_2040 = [54.067, 36.666, 25.855, 23.898]
medium_heavy_transport_2040 = [55.756, 57.357, 56.938, 54.587]
#other_transport_2040 = [14.63, 15.75, 17.70, 19.12]
oil_gas_2040 = [67.312, 48.473, 46.752, 42.691]
industry_2040 = [66.025, 60.643, 70.215, 72.772]
#agriculture_waste_2040 = [82.422, 76.662, 74.455, 72.602]
#utilities_2040 = [3.377, 6.285, 13.445, 18.118]

bar_width = 0.35
bar_positions = np.arange(len(years))

# Plot stacked bar chart for DAC 2035 rollout
plt.figure(figsize=(14, 8))

# Colors as per the request
colors_2035 = ['#0072B2', '#D55E00', '#009E73', '#CC79A7']
colors_2040 = ['#56B4E9', '#FF9933', '#66CC99', '#F0B3D1']

# Arrays to hold the cumulative heights for adding data labels
cumulative_2035 = np.zeros(len(years))
cumulative_2040 = np.zeros(len(years))

def add_labels(positions, heights, bottom):
    for i in range(len(positions)):
        plt.text(positions[i], bottom[i] + heights[i] / 2, f'{heights[i]:.2f}', ha='center', va='center', fontsize=9, color='white')

# DAC 2035 Rollout
#plt.bar(bar_positions - bar_width/2, residential_buildings_2035, width=bar_width, color=colors_2035[0], label='Residential Buildings', zorder=3)
#cumulative_2035 += residential_buildings_2035
#plt.bar(bar_positions - bar_width/2, commercial_buildings_2035, width=bar_width, bottom=cumulative_2035, color=colors_2035[1], label='Commercial Buildings', zorder=3)
#cumulative_2035 += commercial_buildings_2035
plt.bar(bar_positions - bar_width/2, light_transport_2035, width=bar_width, bottom=cumulative_2035, color=colors_2035[0], label='Light Transport', zorder=3)
cumulative_2035 += light_transport_2035
plt.bar(bar_positions - bar_width/2, medium_heavy_transport_2035, width=bar_width, bottom=cumulative_2035, color=colors_2035[1], label='Med/Hvy Transport', zorder=3)
cumulative_2035 += medium_heavy_transport_2035
#plt.bar(bar_positions - bar_width/2, other_transport_2035, width=bar_width, bottom=cumulative_2035, color=colors_2035[4], label='Other Transport', zorder=3)
#cumulative_2035 += other_transport_2035
plt.bar(bar_positions - bar_width/2, oil_gas_2035, width=bar_width, bottom=cumulative_2035, color=colors_2035[2], label='Oil & Gas', zorder=3)
cumulative_2035 += oil_gas_2035
plt.bar(bar_positions - bar_width/2, industry_2035, width=bar_width, bottom=cumulative_2035, color=colors_2035[3], label='Industry', zorder=3)
cumulative_2035 += industry_2035
#plt.bar(bar_positions - bar_width/2, agriculture_waste_2035, width=bar_width, bottom=cumulative_2035, color=colors_2035[7], label='Agriculture & Waste', zorder=3)
#cumulative_2035 += agriculture_waste_2035
#plt.bar(bar_positions - bar_width/2, utilities_2035, width=bar_width, bottom=cumulative_2035, color=colors_2035[8], label='Utilities', zorder=3)
#cumulative_2035 += utilities_2035

'''
# Add data labels for DAC 2035 Rollout
add_labels(bar_positions - bar_width/2, residential_buildings_2035, np.zeros(len(years)))
add_labels(bar_positions - bar_width/2, commercial_buildings_2035, np.array(residential_buildings_2035))
add_labels(bar_positions - bar_width/2, light_transport_2035, np.array(residential_buildings_2035) + np.array(commercial_buildings_2035))
add_labels(bar_positions - bar_width/2, medium_heavy_transport_2035, np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035))
add_labels(bar_positions - bar_width/2, other_transport_2035, np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035))
add_labels(bar_positions - bar_width/2, oil_gas_2035, np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035) + np.array(other_transport_2035))
add_labels(bar_positions - bar_width/2, industry_2035, np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035) + np.array(other_transport_2035) + np.array(oil_gas_2035))
add_labels(bar_positions - bar_width/2, agriculture_waste_2035, np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035) + np.array(other_transport_2035) + np.array(oil_gas_2035) + np.array(industry_2035))
add_labels(bar_positions - bar_width/2, utilities_2035, np.array(residential_buildings_2035) + np.array(commercial_buildings_2035) + np.array(light_transport_2035) + np.array(medium_heavy_transport_2035) + np.array(other_transport_2035) + np.array(oil_gas_2035) + np.array(industry_2035) + np.array(agriculture_waste_2035))
'''

# DAC 2040 Rollout
#plt.bar(bar_positions + bar_width/2, residential_buildings_2040, width=bar_width, color=colors_2040[0], zorder=3)
#cumulative_2040 += residential_buildings_2040
#plt.bar(bar_positions + bar_width/2, commercial_buildings_2040, width=bar_width, bottom=cumulative_2040, color=colors_2040[1], zorder=3)
#cumulative_2040 += commercial_buildings_2040
plt.bar(bar_positions + bar_width/2, light_transport_2040, width=bar_width, bottom=cumulative_2040, color=colors_2040[0], zorder=3)
cumulative_2040 += light_transport_2040
plt.bar(bar_positions + bar_width/2, medium_heavy_transport_2040, width=bar_width, bottom=cumulative_2040, color=colors_2040[1], zorder=3)
cumulative_2040 += medium_heavy_transport_2040
#plt.bar(bar_positions + bar_width/2, other_transport_2040, width=bar_width, bottom=cumulative_2040, color=colors_2040[4], zorder=3)
#cumulative_2040 += other_transport_2040
plt.bar(bar_positions + bar_width/2, oil_gas_2040, width=bar_width, bottom=cumulative_2040, color=colors_2040[2], zorder=3)
cumulative_2040 += oil_gas_2040
plt.bar(bar_positions + bar_width/2, industry_2040, width=bar_width, bottom=cumulative_2040, color=colors_2040[3], zorder=3)
cumulative_2040 += industry_2040
#plt.bar(bar_positions + bar_width/2, agriculture_waste_2040, width=bar_width, bottom=cumulative_2040, color=colors_2040[7], zorder=3)
#cumulative_2040 += agriculture_waste_2040
#plt.bar(bar_positions + bar_width/2, utilities_2040, width=bar_width, bottom=cumulative_2040, color=colors_2040[8], zorder=3)
#cumulative_2040 += utilities_2040

'''
# Add data labels for DAC 2040 Rollout
add_labels(bar_positions + bar_width/2, residential_buildings_2040, np.zeros(len(years)))
add_labels(bar_positions + bar_width/2, commercial_buildings_2040, np.array(residential_buildings_2040))
add_labels(bar_positions + bar_width/2, light_transport_2040, np.array(residential_buildings_2040) + np.array(commercial_buildings_2040))
add_labels(bar_positions + bar_width/2, medium_heavy_transport_2040, np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040))
add_labels(bar_positions + bar_width/2, other_transport_2040, np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040))
add_labels(bar_positions + bar_width/2, oil_gas_2040, np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040) + np.array(other_transport_2040))
add_labels(bar_positions + bar_width/2, industry_2040, np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040) + np.array(other_transport_2040) + np.array(oil_gas_2040))
add_labels(bar_positions + bar_width/2, agriculture_waste_2040, np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040) + np.array(other_transport_2040) + np.array(oil_gas_2040) + np.array(industry_2040))
add_labels(bar_positions + bar_width/2, utilities_2040, np.array(residential_buildings_2040) + np.array(commercial_buildings_2040) + np.array(light_transport_2040) + np.array(medium_heavy_transport_2040) + np.array(other_transport_2040) + np.array(oil_gas_2040) + np.array(industry_2040) + np.array(agriculture_waste_2040))
'''

# Customizing the x-axis with labels and captions
plt.xticks(bar_positions, [f"{year}" for year in years], y=-0.06, fontsize=18, fontweight='bold')  # Move year labels down

# Adding captions for 2035 Rollout and 2040 Rollout above the year labels
for i, pos in enumerate(bar_positions):
    plt.text(pos - bar_width * 0.6, -10, '2035 Rollout', ha='center', va='center', fontsize=14, color='black')
    plt.text(pos + bar_width * 0.6, -10, '2040 Rollout', ha='center', va='center', fontsize=14, color='black')

# Remove the x-axis label
plt.xlabel('')

# Move the legend to the right of the chart, listing only one set of entries
plt.legend(bbox_to_anchor=(0.5, -0.11), loc='upper center', labels=[
    'Light Transport', 'Med/Hvy Transport', 'Oil & Gas', 'Industry'], fontsize=16, ncol=4)

# Remove vertical gridlines
plt.grid(axis='y', zorder=0)  # Only keep horizontal gridlines

plt.ylabel('Emissions (Mt CO$_2$ eq)', fontsize=18, fontweight='bold')
plt.yticks(fontsize=16)
#plt.title('Navius gTech-IESD: Sectoral Emissions by DAC Rollout Year', fontsize=22, fontweight='bold')
plt.tight_layout()
plt.show()






















