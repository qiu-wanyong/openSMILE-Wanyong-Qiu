Copyright Notice
=========
Created on Fri Mar 10 22:38:46 2022

@author: Wanyong Qiu (Executable files)

#### Coding is not easy, please cite the following papers if they are helpful to your learning or writing.
 编码不易，如对您的学习和写作有帮助，请添加引用！BHE小伙伴paper合著能缀本人于末将不甚感谢啦！


Introduction of Program Files
=========

#### 单音频处理
``openSmile-single_wav_LLD.py``
该程序用于处理单个音频.wav数据（通过执行命令）。***单个音频文件LLD特征提取***

#### 多音频批处理
``openSmile-multi_LLD.py``
该程序用于处理多音频.wav数据（通过执行命令）。***多音频文件LLD特征提取***

#### 单数据集批量处理
``openSmile-single_batch.py``
该程序用于处理单个文件夹下的.wav数据（通过执行命令）。***具体适用于某一种类型的语音来进行特征提取***

#### 多数据集批量处理（合并输出）
``openSmile-multiple_batch.py``
该程序用于处理多个文件夹下的.wav数据，会合并多数据集共同提取特征（通过执行命令）。***具体适用于多种不同类型的语音来共同进行特征提取***

#### 单数据集批量处理（Algorithm）
``openSmile_available.py``
该程序用于处理单个数据集的音频并进行特征提取（通过调用opensmile包）。***生成算法可执行的数据格式（行：样本；列：特征），注意：需手动添加 label***

#### 多数据集批量处理（多文件输出）
``openSmile_extract-class.py``
该程序对多文件夹下的wav数据进行批量处理（通过执行命令），并按文件夹名分别输出多个.csv文件。

openSMILE
=========
openSMILE is a versatile and fast open-source toolkit for signal processing and machine learning applications.

**Note:** this is the internal repository of openSMILE that includes proprietary, non-public
components. You can find the open-source repository and official releases on 
[GitHub](https://github.com/audeering/opensmile).

See also the standalone [opensmile](https://github.com/audeering/opensmile-python)
Python package for an easy-to-use wrapper if you are working in Python.

Documentation
-------------

You can find extensive documentation with step-by-step instructions on how to build 
openSMILE and get started at https://audeering.github.io/opensmile/index.html#

Quick start
-----------

For more details on how to customize builds, build for other platforms and use
openSMILE, see Section [Get started](http://tools.pp.audeering.com/opensmile/get-started.html)
in the documentation.


References
-------------
1. [openSMILE 简介](https://blog.csdn.net/qq_22237367/article/details/80897271?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_ecpm_v1~rank_v31_ecpm-2-80897271.pc_agg_new_rank&utm_term=Opensmile%E6%80%8E%E4%B9%88%E5%AD%A6&spm=1000.2123.3001.4430).

2. [opensmile 工具的使用和批处理](https://tobefans.github.io/2020/05/02/opensmile/).

3. [OpenSmile介绍和使用](https://blog.csdn.net/weijie_home/article/details/118754462).

4. [SoX 安装（Ubuntu+win10）的新手误区和正确安装方法](https://blog.csdn.net/qq_35547879/article/details/79700591).

5. [SoX - Sound eXchange Files](https://sourceforge.net/projects/sox/files/sox/).









