import mglearn
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

#인위적인 2차원 데이터 셋 생성 
X , y = make_moons(n_samples=200, noise=0.05, random_state=0)
 
dbscan = DBSCAN() 
dbscan.eps = 0.2  # 간접적으로  클러스터링 수 조절 
clusters = dbscan.fit_predict(X )
 
mglearn.discrete_scatter(X [:,0], X [:,1], clusters  )
plt.legend(["cluster 0","cluster 1","cluster 2"],loc="best")
plt.xlabel("feature 0")
plt.ylabel("feature 1")
plt.show()


