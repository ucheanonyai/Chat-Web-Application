#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:20:37 2020

@author: ucheanonyai
"""

from client import Client
import time
from threading import Thread


name=input("Enter your name ")

c1=Client(name)
time.sleep(3)
while True:
    message=input("")
    if message == "{exit}":
        c1.disconnect()
        break
    else:
        c1.send_message(message)
        time.sleep(1)
    
    
""" 

c1=Client("Uche")

c1.send_message("hey")
time.sleep(5)

c1.send_message("hchhcc")
time.sleep(5)



def update_messages():
    msgs=[]
    while True:
        time.sleep(0.1)
        msgs.extend(c1.get_messages())
        for msg in c1.get_messages():
            print(msg)
            if msg == "{exit}":
                break
 
c1.disconnect()       
#Thread(target=update_messages).start()
"""   