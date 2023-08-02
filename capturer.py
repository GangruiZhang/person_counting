'''
Descripttion: Class for captureing camera
version: V1.0
Author: wangjiaqing
Date: 2023-04-13 18:00:44
LastEditors: sueRimn
LastEditTime: 2023-04-20 17:25:42
'''

import cv2
# from tools.log import Log
# logger = Log(__name__).getLog()
# logger.info("###################### Using Capture.py ############################")

class CameraCap():
    def __init__(self, ip, user, passwd):
        '''
        param: ip: camera ip, user: camera user, passwd: camera user password  
        return {*}
        '''        
        #print("hello __init__!")
        self.url = "rtsp://" + user + ":" + passwd + "@" + ip + ":554/h264/ch1/main/av_stream"
        self._connect()

    def _connect(self):
        self.cap = cv2.VideoCapture(self.url)
        
    def __del__(self):
        #print("hello __del__!")
        self.cap.release()
                   
    def getOneFrame(self):
        if self.cap:
            ret, frame = self.cap.read()
            if not ret:
                self.cap.release()
                self._connect()
            return ret, frame 
        else:
            self._connect()
            return False, None

class VideoCap():
    def __init__(self, videoPath=None):
        '''
        param: ip: camera ip, user: camera user, passwd: camera user password  
        return {*}
        '''        
        #print("hello __init__!")
        self.cap = cv2.VideoCapture(videoPath) if videoPath != None else None
        
    def __del__(self):
        #print("hello __del__!")
        if self.cap != None:
            self.cap.release()

    def resetVideoPath(self, videoPath):
        if self.cap != None:
            self.cap.release()
        self.cap = cv2.VideoCapture(videoPath)
        
    def getOneFrame(self):
        return self.cap.read()
         

if __name__ == "__main__":
    ip = '192.168.6.174'
    user = 'admin'
    passwd = 'hxzh2019'
    test = CameraCap(ip, user, passwd)
    # test = VideoCap('/home/hxzh/01-my_work/02-projects/01-XIZANG_julong_douchi/src.mp4')
    r, frame= test.getOneFrame()
    if r:
        cv2.imwrite("./test.jpg", frame)
    print("done")
    exit()
