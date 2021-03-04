import os 
import cv2
import numpy as np
import argparse
from denoising import denoising
from utils import *

import matlab.engine
import time

eng = matlab.engine.start_matlab()

def main(img,i,name,**args):
    Img = img / 255.

    ImgGray = 0.299*Img[:,:,0]+0.587*Img[:,:,1]+0.114*Img[:,:,2]
    
    starttime = time.clock()
    I_intial0 = Illumination(Img,'max_c')
    
    I_intial = I_intial0.tolist()
    I_optimized = eng.demo_L0_RTV(matlab.double(I_intial))
    I_optimized = np.array(I_optimized)
    
    I_enhances = Adapt_gamma(I_optimized,0.7)
    
    I_unenhence = np.ones(img.shape)
    I_unenhence[:,:,0],I_unenhence[:,:,1],I_unenhence[:,:,2] = I_optimized,I_optimized,I_optimized 
    I_enhence = np.ones(img.shape)
    I_enhence[:,:,0],I_enhence[:,:,1],I_enhence[:,:,2] = I_enhances,I_enhances,I_enhances 
    
    R = Img / I_unenhence

    R_d = guideFilter(Img,R,(35,35),0.00001)
    d = R - R_d 
    R_ref = R_d + 1.3*d
    
    Out_d = R_ref * I_enhence
    
    Out_d = denoising(Out_d)
    endtime = time.clock()
    print('The ' + name+' Time:' +str(endtime-starttime)+'s.') 

    Out = (Out_d*255.).clip(0, 255).astype(np.uint8)
    cv2.imwrite(args['output']+name+'_Out.png',Out)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Low Light Image Enhancement")
    
    parser.add_argument("--input", type=str, default="./image/", \
						help='path to input image')
    parser.add_argument("--output", type=str, default="./Result/", \
						help='path to output image')
    argspar = parser.parse_args()
    
    print("\n### Testing LLIE model ###")
    print("> Parameters:")
    for p, v in zip(argspar.__dict__.keys(), argspar.__dict__.values()):
        print('\t{}: {}'.format(p, v))
    print('\n')
    
    filepath = argspar.input
    files =os.listdir(filepath)


    for i in range (len(files)):
        name = files[i][:-4]
        img = cv2.imread(filepath+ '/'+files[i])
        main(img,i,name,**vars(argspar))