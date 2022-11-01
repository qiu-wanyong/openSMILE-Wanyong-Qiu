"""
ReadMe
***批处理***
该程序用于处理多音频.wav数据（通过执行命令）。***多音频文件LLD特征提取***
Created on Fri Mar 10 21:38:46 2022
@author: Wanyong (Executable file)

"""
import os
from multiprocessing.dummy import Pool as ThreadPool

# Set your opensmile Extracter and path here
exe_opensmile = 'E:/opensmile-3.0.1-win-x64/bin/SMILExtract'
path_config = 'E:/opensmile-3.0.1-win-x64/config/compare16/ComParE_2016.conf'

# Set your data path and output path here
data_path = "E:/opensmile-3.0.1-win-x64/training_pre_data"
save_path = './training_multi-LLD/'  # output folder

# Extractor set-ups
opensmile_options = '-configfile ' + path_config + ' -appendcsvlld 0 -timestampcsvlld 1 -headercsvlld 1'
outputoption = '-lldcsvoutput'


def feature_extract(fn):
    infilename = addr_files + '/' + fn
    instname = os.path.splitext(fn)[0]
    outfilename = save_path + '/' + instname + '.csv'

    opensmile_call = exe_opensmile + ' ' + opensmile_options + ' -inputfile ' + infilename + ' ' + outputoption \
                     + ' ' + outfilename + ' -instname ' + instname + ' -output ?'
    os.system(opensmile_call)


for root, dirs, files in os.walk(data_path):
    for dir in dirs:
        files = os.listdir(data_path + '/' + dir)
        addr_files = data_path + '/' + dir

        pool = ThreadPool()
        pool.map(feature_extract, files)
        pool.close()
        pool.join()
print('over~')
