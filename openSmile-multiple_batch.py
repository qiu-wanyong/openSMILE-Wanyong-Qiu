# -*- coding: utf-8 -*-
"""
ReadMe
**多训练集批量处理**（通过执行命令）
该程序用于处理多个文件夹下的.wav数据（多数据集）。***具体适用于多种不同类型的语音来进行提取特征***
Created on Fri Mar 10 21:38:46 2022
@author: Wanyong (Executable file)

"""

import os
from subprocess import call

# SMILExtract.exe文件路径
pathExcuteFile = r'E:/opensmile-3.0.1-win-x64/bin/SMILExtract.exe'

# opensmile配置文件路径，根据需求选择不同的配置文件
pathConfig = r'E:/opensmile-3.0.1-win-x64/config/compare16/ComParE_2016.conf'

# 读取的数据文件路径。该目录下是各个类别文件夹，类别文件夹下才是wav语音文件,比如说，我的training下有a-f六个训练集，因此对六个训练集一起提取语音特征。
pathAudio = r'E:/opensmile-3.0.1-win-x64/training_multi-dataset/'

# 输出的数据文件路径。注：需先创建feature-wav文件夹
pathOutput = r'E:/opensmile-3.0.1-win-x64/training_multi-dataset/feature-all-wav'

# 利用cmd调用exe文件
def excuteCMD(_pathExcuteFile, _pathConfig, _pathAudio, _pathOutput):
    cmd = _pathExcuteFile + " -C " + _pathConfig + " -I " + _pathAudio + " -O " + _pathOutput
    call(cmd, shell=True)

# 对子目录里所有wav文件进行批处理
def loopExcute(pathwav, patharff):
    for category in os.listdir(pathwav):
        category_path = os.path.join(pathwav, category)
        for file in os.listdir(category_path):
            if os.path.splitext(file)[1] == '.wav':
                file_path = os.path.join(category_path, file)
                name = os.path.splitext(file)[0]
                outputname = 'all_file_feature.csv'  # 将所有的特征文件写入csv文件里
                output_path = os.path.join(patharff, outputname)
                excuteCMD(pathExcuteFile, pathConfig, file_path, output_path)

if __name__ == '__main__':
    # excuteCMD(pathExcuteFile, pathConfig, pathAudio, pathOutput)
    loopExcute(pathAudio, pathOutput)
