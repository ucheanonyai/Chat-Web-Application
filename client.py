#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:16:53 2020

@author: ucheanonyai
"""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock
import time

class Client:
    #for communication with saver.
    #hold all messages and communicate back to server
    
    HOST = "localhost"
    PORT = 5500
    BUFSIZ=512
    ADDR = (HOST, PORT)
    
    def __init__(self,name):
        self.client_socket=socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages=[]
        receive_thread=Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_message(name)
        self.lock=Lock()
        
    def receive_messages(self):
        #receive message from server
        while True:
            try:
                msg=self.client_socket.recv(self.BUFSIZ).decode()
                
                
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
                print(msg)
            
            except Exception as e:
                print("You have left chat ")
                break
        
        
    def send_message(self,msg):
    #send messages to server
    #global client_socket
        try:
            self.client_socket.send(bytes(msg,"utf8"))
    
            if msg == "{exit}":
                self.client_socket.close()
       
        except Exception as e:
            
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            self.client_socket.connect(self.ADDR)
            print(e)
            
    def get_messages(self):
        messages_copy=self.messages[:]
        
        #make sure memory is safe to access
        self.lock.acquire()
        self.messages=[]
        self.lock.release()
        return messages_copy  #list of messages
    
    
    def disconnect(self):
        self.send_message("{exit}")