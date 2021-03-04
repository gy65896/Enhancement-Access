from __future__ import division
from __future__ import print_function
import os, time, scipy.io, shutil
import argparse
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import glob
import re
import cv2

from utils import *
from model import *

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def denoising(a):
    parser = argparse.ArgumentParser(description='Testing on DND dataset')
    parser.add_argument('--cpu', nargs='?', const=1, help = 'Use CPU')
    args = parser.parse_args()
    checkpoint_dir = './checkpoint/' + '/'

# model load
    if os.path.exists(checkpoint_dir + 'checkpoint.pth.tar'):
    # load existing model
        model_info = torch.load(checkpoint_dir + 'checkpoint.pth.tar')
        print('==> loading existing model:', checkpoint_dir + 'checkpoint.pth.tar')
        model = CBDNet()
        if not args.cpu:
            print('Using GPU!')
            model.cuda()
        else:
            print('Using CPU!')
        model.load_state_dict(model_info['state_dict'])
    else:
        print('Error: No trained model detected!')
        exit(1)


   
    model.eval()
    with torch.no_grad():

        noisy_img = a
        noisy_img = noisy_img[:,:,::-1] #/ 255.0
        noisy_img = np.array(noisy_img).astype('float32')

        temp_noisy_img = noisy_img
        temp_noisy_img_chw = hwc_to_chw(temp_noisy_img)

        input_var = torch.from_numpy(temp_noisy_img_chw.copy()).type(torch.FloatTensor).unsqueeze(0)
        if not args.cpu:
            input_var = input_var.cuda()
        _, output = model(input_var)

    output_np = output.squeeze().cpu().detach().numpy()
    output_np = chw_to_hwc(np.clip(output_np, 0, 1))
    Out1 = np.array(np.clip(output_np*255, 0, 255)).astype('float32')/255.
    Out = np.empty(Out1.shape,Out1.dtype)
    Out[:,:,0],Out[:,:,1],Out[:,:,2] = Out1[:,:,2],Out1[:,:,1],Out1[:,:,0]
    return Out

