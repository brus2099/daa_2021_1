# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:45:02 2020

@author: Bruno Cruz Granados
"""

f = open ('Test.js','r')
mensaje = f.read()
print(mensaje)
print(type(mensaje))
f.close()