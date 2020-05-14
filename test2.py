#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:24:36 2020

@author: ucheanonyai
"""

from client import Client
import time
from threading import Thread

name=input("Enter your name ")

c2=Client(name)
time.sleep(3)
while True:
    message=input("")
    if message == "{exit}":
        c2.disconnect()
        break
    else:
        c2.send_message(message)
        time.sleep(1)
    
    
""" 
    c2.send_message("hey")
    time.sleep(5)
    
    c2.send_message("what u talking")
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
 
c2.disconnect()
#Thread(target=update_messages).start()
"""