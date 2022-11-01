Introduction of Program Files
-----------
Created on Fri Mar 10 22:38:46 2022

@author: Wanyong Qiu (Executable files)

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

**Note:** this is the internal repository of openSMILE that includes proprietary, non-public
components. You can find the open-source repository and official releases on 
[GitHub](https://github.com/audeering/opensmile).

See also the standalone [opensmile](https://github.com/audeering/opensmile-python)
Python package for an easy-to-use wrapper if you are working in Python.

Quick start
-----------

For more details on how to customize builds, build for other platforms and use
openSMILE, see Section [Get started](http://tools.pp.audeering.com/opensmile/get-started.html)
in the documentation.

### Linux/MacOS

Prerequisites:
- A version of gcc and g++ or Clang need to be installed that supports C++11.
- CMake 3.5.1 or later needs to be installed and in the PATH.

1. In ``build_flags.sh``, set build flags and options as desired.
2. Run ``bash build.sh``.

Build files will be generated in the ``./build`` subdirectory.
You can find the main SMILExtract binary in ``./build/progsrc/smilextract``.

### Windows

Prerequisites:
- Visual Studio 2017 or higher with C++ components is required.
- CMake 3.15 or later needs to be installed and in the PATH.

1. In ``build_flags.ps1``, set build flags and options as desired.
2. Run ``powershell -ExecutionPolicy Bypass -File build.ps1``.

Build files will be generated in the ``./build`` subdirectory.
You can find the main SMILExtract.exe binary in ``./build/progsrc/smilextract``.

Documentation
-------------

You can find extensive documentation with step-by-step instructions on how to build 
openSMILE and get started at http://tools.pp.audeering.com/opensmile/.
