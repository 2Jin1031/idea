!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

!pip install openpyxl

# Excel 파일을 읽어옵니다.
df = pd.read_excel('/content/drive/MyDrive/visit_history.xlsx', header=None, names = ["date", "visit_count"])

#df.head()
df.head()

df['day'] = ''
df.head()
#df

list = ["목요일", "금요일", "토요일", "일요일", "월요일", "화요일", "수요일"]
list

df['day'] = [list[i % len(list)] for i in range(len(df))]
df.head()

days_order = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font', family='NanumBarunGothic')

df['day'] = pd.Categorical(df['day'], categories=days_order, ordered=True)

# 그래프 그리기
sns.lineplot(x='day', y='visit_count', data=df)
