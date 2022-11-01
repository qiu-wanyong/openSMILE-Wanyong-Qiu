# -*- coding: utf-8 -*-
"""
ReadMe
**单训练集批量处理** (通过调用opensmile包)
该程序用于处理单个训练集的音频数据进行特征提取（批量处理.wav原始文件）。
***生成算法可执行的数据格式（行：样本；列：特征），注意：需手动添加label***
Created on Fri Mar 10 21:38:46 2022
@author: wang and wanyong (Executable file)

"""
import opensmile
import os
import numpy as np
import pandas as pd
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.Functionals,
)
# 处理单个.wav文件
"""
# the result is a pandas.DataFrame containing the features
y = smile.process_file('audio.wav')
data_m = pd.DataFrame(y)
data_m.to_csv('test_data.csv', sep = ',', header=True, index=True)

"""

# 批处理多个.wav文件
path = 'E:/opensmile-3.0.1-win-x64/training_pre_data/c/'

dirs = os.listdir(path)
L = []
M = []
# n=lenth()
for i in dirs:
    y = smile.process_file(path+i)
    L.append(y)

# 输出存储
L = np.array(L)
M = L.reshape((-1, 6373))  # 特征数
Com = pd.DataFrame(M)

# If 存储到Excel中 (需要提前导入库 pip install openpyxl)，Note：跑算法时需手动转换成.csv格式，注意：样本id和label)
# Com.to_excel('./training_data-vailable/f.xlsx')

# If 存储到csv中
Com.to_csv('./training_data-vailable/c2.csv', sep = ',', header=True, index=True)
