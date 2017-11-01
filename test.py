#!user/bin/python
# -*-coding:utf-8-*-

#FileName: test.py
#Version: 1.0
#Author: Jingsheng Tang
#Date: 2017/11/1
#Email: mrtang@nudt.edu.cn
#Github: trzp

from pycamera import PyCamera
from BtRec import ButtonRec
import pygame
from pygame.locals import *
import time
import numpy as np

def test():
    pycam = PyCamera()
    br = ButtonRec('tem.bmp','tem_re.mat',True)
    br.start()
    scr = pygame.display.set_mode(pycam.resolution,1,24)
    while True:
        pygame.event.clear()
        scr.blit(pycam.get['pg_surface'],(0,0))
        pycam.save_to_disk('tem.bmp')

        bts = br.getButtons()
        btns = bts['buttons'].astype(np.float32)
        btns[:,0]-=0.5*btns[:,2]
        btns[:,1]-=0.5*btns[:,3]
        btns = btns.tolist()
        for bt in btns:
            pygame.draw.rect(scr,(255,0,0),bt,1)
        pygame.display.update()

if __name__ == '__main__':
    test()


    
