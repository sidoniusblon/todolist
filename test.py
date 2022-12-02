from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time
import pynput
from pynput.keyboard import Key, Controller
mon = {'top': 0, 'left':960, 'width':540, 'height':1080}
keyboard = Controller()
lower=np.array([23,57,107])
upper=np.array([31,255,255])
sct = mss()
while 1:
    begin_time = time()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2HSV)
    kesilmis=img_bgr[520:600,200:400]
    mask=cv2.inRange(kesilmis,lower,upper)
    number_of_white_pix = np.sum(mask == 255)
    print(number_of_white_pix)
    if(number_of_white_pix>1500):
        keyboard.press('c')
        keyboard.release('c')
        quit()

    cv2.imshow("a",mask)
    cv2.rectangle(img_bgr,(200,520),(400,600),(255,255,255),2)
    cv2.imshow('test', np.array(img_bgr))
    print('This frame takes {} seconds.'.format(time()-begin_time))
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break