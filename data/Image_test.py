from PIL import Image
import torchvision.transforms as transform
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F
from torch.autograd import Variable

path = './out_srf_4_1_005.png'

img = Image.open(path)
img = Variable(transform.ToTensor()(img), requires_grad=False).unsqueeze(0)


if img.shape[2] > img.shape[3]:
    out = F.interpolate(img, size=[1280, 720])
else:
    out = F.interpolate(img, size=[720, 1280])

out_img = transform.ToPILImage()(out[0].data)
out_img.save('new.png')
