#!user/bin/python
# -*-coding:utf-8-*-

#FileName: BtRec.py
#Version: 1.0
#Author: Jingsheng Tang
#Date: 2017/11/1
#Email: mrtang@nudt.edu.cn
#Github: trzp

import thread
import BtRecLib
import scipy.io as sio

class ButtonRec:
    def __init__(self,image_path,result_path,down_sample=True):
        self.BtRec = BtRecLib.initialize()
        self.image_path = image_path
        self.result_path = result_path
        self.down_sample = down_sample
        self.__buttons = {'num':0,'buttons':None}

    def start(self):
        thread.start_new_thread(self.BtRec.start,(self.image_path,self.result_path,int(self.down_sample)))

    def getButtons(self):
        try:
            r = sio.loadmat(self.result_path)['buttons']
            self.__buttons['num'] = r.shape[0]
            self.__buttons['buttons'] = r
        except:
            pass
        return self.__buttons


