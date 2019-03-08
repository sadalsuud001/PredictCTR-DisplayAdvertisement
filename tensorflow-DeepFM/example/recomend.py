import pandas as pd
import numpy as np

threshold = 0.7
df = pd.read_csv('out/recommend.csv')
users = df[df['Predict'] > threshold]
recommend_users = users.user.unique()

