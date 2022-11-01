# encoding = utf-8
"""
**多训练集批量处理**（通过执行命令）
该程序对多文件夹下的wav数据进行批量处理，并按文件夹名输出多个csv文件。
Created on Fri Mar 10 21:38:46 2022
@author: ComputerAudition_class (Executable file)

"""
import os
import glob

# opensmile 执行文件和配置文件路径
SMILExtract_path = 'E:/opensmile-3.0.1-win-x64/bin/SMILExtract'
SMILEconf_path = 'E:/opensmile-3.0.1-win-x64/config/compare16/ComParE_2016.conf'

def main():
    dirPath = glob.glob('E:\\opensmile-3.0.1-win-x64\\training_pre_data\\*')  # 读取文件夹下的子目录
    features_folder = './training_extract-class/'  # 特征存储路径
    for folder in dirPath:
        extract_smile(folder, features_folder)

    # # 音频文件位置
    # input_file = './opensmile.wav'
    # # 特征文件
    # output_file = './output_file.csv'
    # output_file_lld = './output_file_lld.csv'
    #
    # extract_smile(input_file,output_file,output_file_lld)

def extract_smile(audio_folder, features_folder):
    if audio_folder[-1] != '\\':
        audio_folder += '\\'
    if features_folder[-1] != '/':
        features_folder += '/'

    if not os.path.isdir(features_folder):
        os.mkdir(features_folder)

    audio = audio_folder.split('\\')[-2]
    print(audio_folder)
    print(audio)

    output_file = features_folder + audio + '.csv'
    output_file_lld = features_folder + audio + 'LLD.csv'
    if os.path.exists(output_file):
        os.remove(output_file)
    if os.path.exists(output_file_lld):
        os.remove(output_file_lld)

    files = os.listdir(audio_folder)
    for file in files:
        print(file)
        input_file = os.path.join(audio_folder, file)
        # 通过命令行方式提取特征
        os.system(SMILExtract_path + ' -C ' + SMILEconf_path + ' -I ' + input_file + ' -instname ' + input_file + ' -csvoutput ' + output_file + ' -timestampcsv 0 -lldcsvoutput ' + output_file_lld + ' -appendcsvlld 1')


if __name__ == "__main__":
    main()
