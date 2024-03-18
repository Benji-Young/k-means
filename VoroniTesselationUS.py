import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import pyplot as plt
import pandas as pd

state_data = pd.read_csv("states.csv")
coordinates = state_data[["longitude", "latitude"]].to_numpy()

# Choose your colors here (e.g., RGB values)
colours = []
for i in range(len(coordinates)):
    colours.append((np.random.choice(range(256), size=3)).tolist())

#plt.scatter(coordinates[:,0], coordinates[:,1])

vor = Voronoi(coordinates)

# Plot the Voronoi diagram with custom colors
fig = voronoi_plot_2d(vor, show_vertices = False)

# colorize
for region in vor.regions:
    polygon = vor.vertices[region]
    plt.fill(*zip(*polygon), alpha=0.4)

plt.plot(coordinates[:,0], coordinates[:,1], 'ko')

plt.show()

