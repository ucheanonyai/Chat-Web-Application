# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from Person import Person

HOST = 'localhost'
PORT=5500
BUFSIZ = 512 #how big messages would be(how many bits of data)
ADDR = (HOST,PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

persons=[] #list of people in chat

def broadcast(msg, name):
    #send message to all clients
    
    for person in persons:
        print(person)
        client = person.client

        try:
            
            client.send(bytes(name, "utf8") + msg)
        except Exception as e:
            print("[EXCEPTION]", e)

def client_communication(person): #create client object with address and name
   #handle messages from clients
   client=person.client
   
   addr=person.addr
   
   #get persons namee
   name=client.recv(BUFSIZ).decode("utf8")
   person.set_name(name)
   msg=bytes(f"{name} has joined chat","utf8")
   broadcast(msg, "")
   
   while True:
       try:
            msg=client.recv(BUFSIZ)
            print(f"{name}:", msg.decode("utf8"))
        
            if msg == bytes("{exit}","utf8"):
                client.close()
                persons.remove(person)
                broadcast(bytes(f"{name} has left the chat...","utf8"),"")
               # client.send(bytes("{exit}","utf8"))
                break
            else:
                broadcast(msg,name + ": ")
            
       except Exception as e:
            print("Errors ", e)
            break

def wait_for_connection():
    #start new thread when new client is connected
    while True:
        try:
            client, addr= SERVER.accept()
            person = Person(addr, client)
            persons.append(person) #adding person object o list of persons
            Thread(target=client_communication, args=(person,)).start()
            print("[Connection]",addr,"connected to server at",time.time())
        except Exception as e:
            print("Error",e)
            break
            
    print("Server crashed")
            
            



if __name__ == "__main__":
    SERVER.listen(10) #listen for 10 connections
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()