import mglearn
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#인위적인 2차원 데이터 셋 생성 
X_varied, y_varied = make_moons(n_samples=200, noise=0.05, random_state=0)
 
# 3개의 클러스터 생성 
y_pred = KMeans(n_clusters=3).fit_predict(X_varied)

mglearn.discrete_scatter(X_varied[:,0], X_varied[:,1], y_pred)
plt.legend(["cluster 0","cluster 1","cluster 2"],loc="best")
plt.xlabel("feature 0")
plt.ylabel("feature 1")
plt.show()

