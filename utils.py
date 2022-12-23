import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 데이타 합치기
def get_data(col='close'):
  groupD = pd.read_csv('data/group_D.csv', usecols=[col])
  groupC = pd.read_csv('data/group_C.csv', usecols=[col])
  groupB = pd.read_csv('data/group_B.csv', usecols=[col])
  groupA = pd.read_csv('data/group_A.csv', usecols=[col])
  
  # 최근 가격을 위로
  return np.array([groupD[col].values[::-1], 
                  groupC[col].values[::-1],
                  groupB[col].values[::-1],
                  groupA[col].values[::-1],
                  ])

# env 가져오고 스케일러 반환
def get_scaler(env):
  low = [0] * (env.n_stock * 2 + 1)

  high = []
  max_price = env.stock_price_history.max(axis=1)
  min_price = env.stock_price_history.min(axis=1)
  max_cash = env.init_invest * 3 
  max_stock_owned = max_cash // min_price
  for i in max_stock_owned:
    high.append(i)
  for i in max_price:
    high.append(i)
  high.append(max_cash)
# 평균 0 분산 1로 스케일 조정(정규화)
  scaler = StandardScaler()
  scaler.fit([low, high])
  return scaler


def maybe_make_dir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)