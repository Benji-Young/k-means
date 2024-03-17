import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Collect the data
df = pd.read_csv("values.csv")
df = df.drop(["id"], axis=1)

k = 4

# Perform k-means
km = KMeans(n_clusters=k, init='k-means++', random_state=0)
km.fit(df)
labels = km.labels_

# Create a colour map
cmap = plt.get_cmap("viridis")
colors = [cmap(i) for i in np.linspace(0, 1, k)]

# Plot the results
plt.scatter(df["x"], df["y"], c=km.labels_.astype('int'), cmap='viridis')
# Plot the centroids
for i in range(k):
    plt.scatter(km.cluster_centers_[i,0], km.cluster_centers_[i,1], c=colors[i], marker="*", s=100)

plt.title("K-Means Clustering with k = 4")
#plt.scatter(df["x"], df["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print(km.labels_)
