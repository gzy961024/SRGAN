from PIL import Image
import os


def gen_image_set(path, des_path):
    data_path = path + 'zte_data/'
    for img_num in os.listdir(data_path):
        max_pix = 0
        max_name = ''
        pic_path = data_path + img_num + '/'
        for img_name in os.listdir(pic_path):
            img = Image.open(pic_path + img_name)
            pix = img.size[0] * img.size[1]
            if (pix > max_pix):
                max_pix = pix
                max_name = pic_path + img_name
        os.system('cp %s %s' % (max_name, des_path))


if not os.path.exists('./new'):
	os.mkdir('./new')
gen_image_set('./','./new')
