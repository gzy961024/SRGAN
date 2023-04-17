import os

import torch
from PIL import Image
from torch.autograd import Variable
from torchvision.transforms import ToTensor, ToPILImage

from model import Generator

img_path = './data/new/'
out_path = './data/new/proc_img/'
if not os.path.exists(out_path):
    os.mkdir(out_path)
device = 'cuda:1'
torch.cuda.set_device(device)


def main(input_path, output_path):
    MODEL_NAME = 'netG_epoch_4_99.pth'
    UPSCALE_FACTOR = 4

    model = Generator(UPSCALE_FACTOR).eval()
    model.cuda()
    model.load_state_dict(torch.load('./epochs/' + MODEL_NAME))

    for img_name in os.listdir(input_path):
        img = Image.open(input_path + img_name)
        img = Variable(ToTensor()(img), requires_grad=False).unsqueeze(0)
        img = img.cuda()

        out = model(img)

        out_img = ToPILImage(out[0].data.cpu())
        out_img.save(out_path + 'out_srf_' + str(UPSCALE_FACTOR) + '_' + img_name)


main(img_path, out_path)
