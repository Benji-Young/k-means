import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import pyplot as plt
import pandas as pd
import helper

state_data = pd.read_csv("states.csv")
coordinates = state_data[["longitude", "latitude"]].to_numpy()

# Choose your colors here (e.g., RGB values)
colours = []
for i in range(len(coordinates)):
    colours.append((np.random.choice(range(256), size=3)).tolist())

#plt.scatter(coordinates[:,0], coordinates[:,1])

vor = Voronoi(coordinates)
# Get the finite regions
regions, vertices = helper.voronoi_finite_polygons_2d(vor)

# Colourize the regions
for region in regions:
    polygon = vertices[region]
    plt.fill(*zip(*polygon), alpha=0.9)

plt.plot(coordinates[:,0], coordinates[:,1], 'ko')
plt.xlim(min(coordinates[:,0])-10, max(coordinates[:,0])+10)
plt.ylim(min(coordinates[:,1])-10, max(coordinates[:,1])+10)
plt.show()

