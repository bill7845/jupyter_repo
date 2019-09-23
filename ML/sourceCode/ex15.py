import pandas as pd 
from sklearn.cluster import KMeans

data =pd.read_csv("ex15_academy.csv")
#print( data.iloc[:,1:] )  
 
# 군집 모델을 만듭니다
kmeans = KMeans(n_clusters=3)
kmeans.fit( data.iloc[:,1:]  ) #학생번호 컬럼은 제외하고 학습 
 
for no, cla in enumerate(kmeans.labels_):
    print("학생번호: {} : {}".format(no, cla))
 
# 국어점수 100, 영어점수 80,
# 수학점수 70,  과학점수 70, 학업성취도 70
# 인 새로운 학생이 입학하였습니다. 
# 이 학생은 몇번 클러스터에 포함되어야 합니까?  

print(kmeans.predict([[100,80,70,70,70]]))   




