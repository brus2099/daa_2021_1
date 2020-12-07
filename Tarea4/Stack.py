# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:12:47 2020

@author: Bruno Cruz Granados
"""

# Class stack

class Stack:
  def __init__( self ):
    self.__datos = []

  def is_empty( self ):
    return len(self.__datos) == 0

  def get_top( self ):
    return self.__datos[-1]

  def pop( self ):
    self.__datos.pop()

  def push( self, valor ):
    self.__datos.append(valor)

  def get_length( self ):
    return len(self.__datos)

  def to_string( self ):
    print('-----')
    for ele in self.__datos[-1::-1]:
      print(f' {ele} ')
    print('-----')