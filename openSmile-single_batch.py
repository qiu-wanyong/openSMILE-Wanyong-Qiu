# -*- coding: utf-8 -*-
"""
ReadMe
**单训练集批量处理**
该程序用于处理单个文件夹下的.wav数据（通过执行命令）。***具体适用于某一种类型的语音来进行提取特征***
Created on Fri Mar 10 21:38:46 2022
@author: Wanyong (Executable file)

"""

import os
from subprocess import call

def excute_CMD(path_ExcuteFile, path_Config, path_Audio, path_Output):
    cmd = path_ExcuteFile + " -C " + path_Config + " -I " + path_Audio + " -O " + path_Output
    call(cmd, shell=True)

def batch_extract_features(path_Config, path_Input_Root, path_Output):
    path_ExcuteFile = "E:/opensmile-3.0.1-win-x64/bin/SMILExtract"

    filename = os.listdir(path_Input_Root)
    for i in range(len(filename)):
        print('Extracting features of %s' % filename[i])
        # path_Input = path_Input_Root + '/' + filename[i] + '.wav'
        path_Input = path_Input_Root + '/' + filename[i]
        excute_CMD(path_ExcuteFile, path_Config, path_Input, path_Output)

path_Config = "E:/opensmile-3.0.1-win-x64/config/compare16/ComParE_2016.conf"
path_Input_Root = 'E:/opensmile-3.0.1-win-x64/training_single-batch/validation'  # wav子目录
path_Output = 'E:/opensmile-3.0.1-win-x64/training_single-batch/feature-wav/val-file-feature.csv'  # 输出csv文件
batch_extract_features(path_Config, path_Input_Root, path_Output)
