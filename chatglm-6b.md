# chatglm-6b 
## 系统环境
```shell
nvidia-smi
nvcc -V

# 安装nvsmi
# Microsoft 基本显示适配器
# DxDiag
# C:\Program Files\NVIDIA Corporation\NVSMI
# CUDA Toolkit安装教程（Windows）
# https://www.nvidia.cn/Download/index.aspx?lang=cn
# 最新版本：https://developer.nvidia.com/cuda-downloads
# 历史版本：https://developer.nvidia.com/cuda-toolkit-archive
```

## 本地化部署
### 环境准备
```shell
conda create -n chatglm python=3.11.5
conda activate chatglm

conda create --name pytorch1.12 python=3.9
conda activate pytorch1.12
conda install pytorch=1.12 torchvision torchaudio -c pytorch
pip install tensorflow

conda create --name pytorch2.0 python=3.9
conda activate pytorch2.0
conda install pytorch=2.0 torchvision torchaudio -c pytorch
pip install tensorflow

conda activate pytorch1.12
jupyter notebook
import torch
print(torch.__version__)

import tensorflow as tf
print(tf.__version__)

```

### 下载代码仓
```shell
git clone git@github.com:THUDM/ChatGLM-6B.git
```

### 安装依赖
```shell
cd ChatGLM-6B
pip install -r requirements.txt

# 清华镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 下载模型
```shell
git clone https://huggingface.co/THUDM/chatglm-6b

# 清华
https://openai.wiki/chatglm-6b.html
https://cloud.tsinghua.edu.cn/d/674208019e314311ab5c/

```

### 相关资源
https://www.langchain.com.cn/

https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide

https://github.com/yzfly/awesome-chatgpt-zh


https://github.com/yanqiangmiffy/Chinese-LangChain

https://github.com/gottaBoy/Langchain-Chatchat

https://github.com/chatchat-space/Langchain-Chatchat

https://openi.pcl.ac.cn/Learning-Develop-Union/LangChain-ChatGLM-Webui

