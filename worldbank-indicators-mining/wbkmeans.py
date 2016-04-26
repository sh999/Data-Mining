'''
Kmeans clustering of world data bank data using 2 indicators
'''

import wbdata
import datetime
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import time
from sklearn.datasets.samples_generator import make_blobs

#countries = [i['id'] for i in wbdata.get_country(incomelevel="OEC", display=False)]
#countries = [i['id'] for i in wbdata.get_country(country_id=None, display=False)]
indicators = {"SP.URB.TOTL.IN.ZS": "urban%","NY.GDP.PCAP.PP.KD": "gdppc"}
#indicators = {"NY.GDP.PCAP.PP.KD": "gdppc"}
data_date = (datetime.datetime(2011,1,1), datetime.datetime(2011,1,1))
df = wbdata.get_dataframe(indicators, country="all", convert_date=True, data_date=data_date)
df = df.fillna(df.mean())   # replace missing values with mean
#print (df.describe())
print (df.values)   


# most of the code on kmeans were taken from scikit site

centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.7)
X = df.values   # This is where the wdb data frame is put in the Kmeans as X


k_means = KMeans(init='k-means++', n_clusters=3, n_init=10)
t0 = time.time()
k_means.fit(X)
t_batch = time.time() - t0
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_
k_means_labels_unique = np.unique(k_means_labels)



n_clusters = 3
fig = plt.figure(figsize=(16, 6))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)
colors = ['#4EACC5', '#FF9C34', '#4E9A06']
# KMeans
ax = fig.add_subplot(1, 3, 1)
#I hthink this is the plotting of individual dots
for k, col in zip(range(n_clusters), colors):
    my_members = k_means_labels == k
    cluster_center = k_means_cluster_centers[k]
    ax.plot(X[my_members, 0], X[my_members, 1], 'w',
            markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
            markeredgecolor='k', markersize=6)
ax.set_title('KMeans')
#ax.set_xticks(())
#ax.set_yticks(())
plt.ylabel(df.columns.values[1])    # label axes
plt.ylabel(df.columns.values[0])    # label axes
plt.text(-3.5, 1.8,  'train time: %.2fs\ninertia: %f' % (
    t_batch, k_means.inertia_))


plt.show()