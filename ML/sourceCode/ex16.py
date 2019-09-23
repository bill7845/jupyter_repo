import mglearn
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

#인위적인 2차원 데이터 셋 생성 
X_varied, y_varied = make_blobs(n_samples=600,random_state=170)

#데이터가 길게 늘어지도록 변경 
rng = np.random.RandomState(74)
transformation = rng.normal(size = (2,2))
X_varied = np.dot(X_varied, transformation)

# 3개의 클러스터 생성 
y_pred = KMeans(n_clusters=3).fit_predict(X_varied)

mglearn.discrete_scatter(X_varied[:,0], X_varied[:,1], y_pred)
plt.legend(["cluster 0","cluster 1","cluster 2"],loc="best")
plt.xlabel("feature 0")
plt.ylabel("feature 1")
plt.show()
