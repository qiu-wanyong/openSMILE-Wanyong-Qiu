"""
ReadMe
***单音频处理***
该程序用于处理单个音频.wav数据（通过执行命令）。***单个音频文件LLD特征提取***
Created on Fri Mar 10 21:38:46 2022
@author: Wanyong (Executable file)

"""
import os

infilename = 'E:/opensmile-3.0.1-win-x64/training_pre_data/a/a0002.wav'
outfilename = 'E:/opensmile-3.0.1-win-x64/training_single-batch/feature-single/a0002.csv'

# 设置OpenSmile路径
exe_opensmile = 'E:/opensmile-3.0.1-win-x64/bin/SMILExtract'
# 选择并设置使用的配置文件
path_config = 'E:/opensmile-3.0.1-win-x64/config/compare16/ComParE_2016.conf'

# 设置系统命令
opensmile_options = '-configfile ' + path_config + ' -appendcsvlld 0 -timestampcsvlld 1 -headercsvlld 1'
outputoption = '-lldcsvoutput'
opensmile_call =exe_opensmile + ' ' + opensmile_options + ' -inputfile ' + infilename + ' ' + outputoption + ' ' + outfilename
# 执行
os.system(opensmile_call)
print('over~')
