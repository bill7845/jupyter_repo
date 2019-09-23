import mglearn
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc 
from sklearn.datasets import load_breast_cancer
import numpy as np
import matplotlib

#한글 폰트 등록
font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

cancer = load_breast_cancer() #breast_cancer sample 데이터

# 특성이 30개이므로  15X2  set의 plot 객체 생성합니다.
fig, axes = plt.subplots(15, 2, figsize=(10,20)) 

malignant = cancer.data[cancer.target == 0]     #악성 데이터 
benign = cancer.data[cancer.target == 1]        #양성 데이터  
target_set = np.array([malignant, benign])
ax = axes.ravel()

for i in range(30) :
    a, bins = np.histogram(cancer.data[:,i], bins=50)# bins: histogram 간격
    ax[i].hist(malignant[:,i], bins=bins,color="red", alpha=0.5)
    ax[i].hist(benign[:,i],    bins=bins,color=mglearn.cm3(2), alpha=0.5)
    ax[i].set_title(cancer.feature_names[i])
    ax[i].set_yticks(())   # y 눈금 지움

ax[0].set_ylabel('frequency')
ax[0].legend(['악성 ', '양성 '], loc="best" )
fig.tight_layout()
plt.show()

 

