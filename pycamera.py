#!user/bin/python
# -*-coding:utf-8-*-

#FileName: pycamera.py
#Version: 1.0
#Author: Jingsheng Tang
#Date: 2017/11/1
#Email: mrtang@nudt.edu.cn
#Github: trzp


from VideoCapture import Device
import pygame
import numpy as np

class PyCamera:
    def __init__(self,device_num = 0):
        self.cam = Device(device_num)
        self.resolution = self.cam.getBuffer()[1:3]

    @property
    def get(self):
        '''
        return: {'buffer':**,'pixels':**,'pg_surface':**,'resolution':**}
        '''
        # 推荐使用getImage，getImage能显著提高图像质量，并且自动完成图像的翻转等操作
        # buffer,width,height = self.cam.getBuffer()

        image = self.cam.getImage()
        buffer = image.tostring()
        sur = pygame.image.frombuffer(buffer,self.resolution,'RGB')
        pixels = np.fromstring(buffer,dtype = np.uint8)
        return {'buffer':buffer,'pixels':pixels,'pg_surface':sur,'resolution':self.resolution}

    def save_to_disk(self,filename):
        self.cam.saveSnapshot(filename)