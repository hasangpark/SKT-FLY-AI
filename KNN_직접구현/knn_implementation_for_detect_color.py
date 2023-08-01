import cv2
import numpy as np
from matplotlib import pyplot as plt

# 각 데이터의 위치: 25 X 2 크기에 각각 0 ~ 100
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
# 각 데이터는 0 or 1
response = np.random.randint(0, 2, (25, 1)).astype(np.float32)

# 값이 0인 데이터를 각각 화면 (x, y) 위치에 빨간색으로 칠합니다.
red = trainData[response.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
# 값이 1인 데이터를 각각 화면 (x, y) 위치에 파란색으로 칠합니다.
blue = trainData[response.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

# (0 ~ 100, 0 ~ 100) 위치의 데이터를 하나 생성해 칠합니다.
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

from collections import counter #필요한 라이브러리 임포트
total=[] #거리를 넣을 리스트 생성
for i in blue : #라벨과 X,Y값 APPEND
    total.append([i[0],i[1],1])
for i in red : #라벨과 X,Y값 APPEBD
    total.append([i[0],i[1],0])
ans=[]
for i in total : #모든 값들 거리 계산해서 라벨과 거리 ANS에 APPEND
    ans.append([np.sqrt((i[0]-newcomer[0][0])**2 + (i[1]-newcomer[0][1])**2),i[2]])
ans.sort() #거리순으로 정렬
answer=ans[:3] # 3순위까지 뽑기
neighbours=[]
dist=[]
for i in answer :  #라벨이 더 많은 걸로 색깔 결정
    neighbours.append(i[1])
    dist.append(i[0])
label_cnt= counter(neighbours)
if label_cnt[0] > label_cnt[1] :
    results=0
else :
    results=1
    
# 가까운 3개를 찾고, 거리를 고려하여 자신을 정합니다.
print("result : ", results)
print("neighbours :", neighbours)
print("distance: ", dist)
plt.show()


# 가까운 3개를 찾고, 거리를 고려하여 자신을 정합니다.
print("result : ", results)
print("neighbours :", neighbours)
print("distance: ", dist)
plt.show()