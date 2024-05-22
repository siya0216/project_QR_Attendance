import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64



cap = cv2.VideoCapture(0)

names =[]

fob=open('attendence.txt ','a+')
def enterDate(z):
    if z in names:
        pass
    else:
        nmaes.append(z)
        z=".join(str(z))
        fob.write(z+'\n')
        return names


print('READING CODE...........')



def checkData(data):
data =str(data)
if data in names:
print('Already present..')
else:
     print('\n'+str(len(names)+1)+'\n'+'Present done')
     enterData(data)



while True:
_,frame = cap.read()
decodeObject =pyzbar.decode(frame)
for obj in decodeObject:
chechData(obj.data)
time.sleep(1)

cv2.imshow('Frame',frame)

  if cv2.waitkey(1)&0xff==ord('s'):
      cv2.destroyAllWindows()
      break
fob.close()