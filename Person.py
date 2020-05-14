#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:00:57 2020

@author: ucheanonyai
"""
#has persons name, ip address
class Person:
    def __init__(self,addr, client):
        self.addr=addr
        self.name=None
        self.client=client
        
    def __repr__(self):
        return f"Person({self.addr},{self.name})"
    
    def set_name(self,name):
        self.name=name