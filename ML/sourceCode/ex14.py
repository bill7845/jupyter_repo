import mglearn
import pandas as pd 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

data =pd.read_csv("ex14_academy.csv" )
print( data.iloc[:,1:] )
 
# 군집 모델을 만듭니다
kmeans = KMeans(n_clusters=3)
kmeans.fit(data.iloc[:,1:])

print("클러스터 레이블 ", kmeans.labels_) 

mglearn.discrete_scatter(data.iloc[:,1], data.iloc[:,2], kmeans.labels_)
plt.legend(["클러스터 0", "클러스터 1", "클러스터 2"], loc='best')
plt.xlabel("국어점수 ")
plt.ylabel("영어점수 ")
plt.show()


# 국어점수 100, 영어점수 80 인 새로운 학생이 입학하였습니다. 
# 이 학생은 몇번 클러스터에 포함되어야 합니까?  
print(kmeans.predict([[100,80]])) 
plt.show()

