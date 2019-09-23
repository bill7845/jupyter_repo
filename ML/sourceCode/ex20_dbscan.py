import mglearn
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

#인위적인 2차원 데이터 셋 생성 
X , y  = make_blobs(n_samples=200, random_state=0)
  
dbscan = DBSCAN() 

clusters = dbscan.fit_predict(X )

mglearn.discrete_scatter(X [:,0], X[:,1], clusters) 
plt.xlabel("feature 0")
plt.ylabel("feature 1")
plt.show()


