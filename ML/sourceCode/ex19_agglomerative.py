import mglearn
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

#인위적인 2차원 데이터 셋 생성 
X , y  = make_blobs( random_state=1)

# 3개의 클러스터 생성 
agg= AgglomerativeClustering(n_clusters=3)
assignment = agg.fit_predict(X)

mglearn.discrete_scatter(X [:,0], X [:,1], assignment)
plt.legend(["cluster 0","cluster 1","cluster 2"],loc="best")
plt.xlabel("feature 0")
plt.ylabel("feature 1")
#plt.show()



