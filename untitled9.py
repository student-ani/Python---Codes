import pandas as pd
df = pd.read_csv("C:\Users\hp\Downloads\CAP450\diabetes.csv")
print(df.head())

import numpy as np
max_val = np.max(np.abs(df))
max_val

print ((df-max_val)/max_val)

from re import S
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
                         columns = df.columns)
print(scaled_df.head())

from sklearn.preprocessing import Normalizer
scaler = Normalizer()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
                         columns = df.columns)
print (scaled_df.head())

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
                         columns = df.columns)
print (scaled_df.head())

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
scaler_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
                         columns = df.columns)
print (scaled_df.head())

