# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:11:11 2020

@author: Bruno Cruz Granados
"""

from Stack import Stack

f = open ('Matrices.c','r')
message = f.read()

"""
cadena_a_evaluar = "(true);\
((number);('hello'));"
"""

my_program = Stack()
balance = Stack()
no_chars = False

for i in message:
    my_program.push(i)

for i in range(my_program.get_length()):
    actual_char = my_program.get_top()
    
    # Rompe instantaneamente porque se ha encontrado un caracter de apertura sin haber caracteres en pila pendientes
    if (actual_char == '(' or actual_char == '[' or actual_char == '{') and balance.get_length() == 0:
        no_chars = True
        print('Error: no habia caracter de cierre...')
        break
    
    # Si se encuentra un cierre de caracter, se añade a una pila para esperar su cierre
    if actual_char == ')' or actual_char == ']' or actual_char == '}':
        balance.push(actual_char)
        print(f'{actual_char} --> esperando cierre!!!! ahora {balance.get_length()} restantes')
    
    # El caracter guardado en la pila se saca solo si el de apertura coincide
    if (actual_char == '(' and balance.get_top() == ')') or (actual_char == '[' and balance.get_top() == ']') or (actual_char == '{' and balance.get_top() == '}'):
        balance.pop()
        print(f'{actual_char} --> cierra pila, {balance.get_length()} restantes, cierre exitoso...')
    # Si el caracter no coincide, el flujo se evalua como desbalance, con caracteres pendientes en la pila
    elif (actual_char == '(' and balance.get_top() != ')') or (actual_char == '[' and balance.get_top() != ']') or (actual_char == '{' and balance.get_top() != '}'):
        print('Error: caracter no coincide con el ultimo cierre. Saliendo...')
        break
        
    my_program.pop()
    
# No debe haber caracteres guardados en la pila
print(f'restantes en pila: {balance.get_length()}')
f.close()

if no_chars or balance.get_length() > 0:
    print('desbalance!!!')
else:
    print('balance!')

# Follow me! @brus2099

