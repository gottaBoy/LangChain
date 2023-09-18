# 如何查看pytorch、cuda、cuddn、torch和torchvision的版本并且进行下载安装
import torch
import torchvision

cuda_is_av = torch.cuda.is_available()   # 检查cuda是否可用
cuda_version = torch.version.cuda          # 查看cuda版本

print(cuda_is_av)
print(cuda_version)

torch.__version__
torchvision.__version__
torch.backends.cudnn.is_available()  # 检查cudnn是否可用
torch.backends.cudnn.version()       # 查看cudnn版本