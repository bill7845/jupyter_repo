import mglearn
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

#한글 폰트 등록
font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

# 인위적으로 2차원 데이터를 생성합니다 
X,y = make_blobs(random_state=1)
print(X)

# KMeans 3개의 클러스터로 군집화  
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

print(kmeans.labels_) # 클러스터링한 결과 라벨 
 
mglearn.discrete_scatter(X[:,0], X[:,1], kmeans.labels_, markers='^')
# 세번째 매개인자인  클러스터링한 결과 라벨 (kmeans.labels_) 별로 다른 색 그래프 
# x축 X[:,0],  y축 X[:,1] 
plt.show()

#######################################################################
fig, axes = plt.subplots(1,2,figsize=(10,5))   #1행 2열 sub그래프
 
#두 개의 클러스터 중심을 사용
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
assignments = kmeans.labels_
mglearn.discrete_scatter(X[:,0],X[:,1],assignments, ax = axes[0])

#######################################################################
#다섯 개의 클러스터 중심
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
assignments = kmeans.labels_  

mglearn.discrete_scatter(X[:,0],X[:,1],assignments, ax = axes[1]) 

plt.legend(["클러스터1","클러스터2","클러스터3","클러스터4","클러스터5"])
plt.ylabel("특성1")
plt.xlabel("특성0")
plt.show()

