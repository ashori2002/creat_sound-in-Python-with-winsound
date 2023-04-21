import winsound as ws
from random import randint as rn

def creat_sound ():

    while True:
        ws.Beep(rn(50 , 2000) , rn(200 , 1000))
