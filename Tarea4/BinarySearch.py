
import math
new_list = [1, 2, 3, 4, 5, 6, 7]

searched = -1

def recursive_bs( list, sear ):
    
    mid = len(list)/2
    
    if sear == list[ int( math.floor( mid ) ) ]:
        return True

    elif sear > list[ len( list ) - 1 ] or sear < list[ 0 ]:
        return False
    
    elif sear < list[ int( math.floor( mid ) ) ]:
        recursive_bs( list[ 0:int( math.floor( mid ) ) ], sear )

    elif sear > list[ int( math.floor( mid ) ) ]:
        recursive_bs( list[ int( math.floor( mid ) ):len(list) ], sear )
        
# Uso del la funcion recursive_bs( lista, numero_buscado )
# recursive_bs(new_list, searched)

def verify_student( id, database ):
    
    ordered_list = []
    
    for i in range ( len(database) ):
        print(database[i]["id"])
        ordered_list.append( database[ i ][ "id" ] )

    print(ordered_list, id)
    data = recursive_bs( ordered_list, id )
    print(data)

    if data:
        index = ordered_list.index( data )
        print(index)
        print( f'{ database[index]["nombre"] } estudia la carrera de { database[index]["carrera"] } y tiene un promedio de { database[index]["promedio"] }' )
    else:
        print('El alumno no existe en la base de datos.')



alumno1={'id':2, 'nombre':"Juan" , 'carrera':"ICO", 'promedio':7.67}
alumno2={'id':4, 'nombre':"Rocio" , 'carrera':"ICI", 'promedio':8.67}
alumno3={'id':5, 'nombre':"Diego" , 'carrera':"DER", 'promedio':8.98}
alumno4={'id':7, 'nombre':"May" , 'carrera':"ICI", 'promedio':9.87}
alumno5={'id':9, 'nombre':"Rob" , 'carrera':"IME", 'promedio':10.00}
alumno6={'id':10, 'nombre':"Santi" , 'carrera':"ICO", 'promedio':5.37}
alumno7={'id':14, 'nombre':"Moy" , 'carrera':"IME", 'promedio':6.85}
alumno8={'id':16, 'nombre':"Diana" , 'carrera':"DER", 'promedio':9.99}
alumno9={'id':19, 'nombre':"Zoila" , 'carrera':"ICO", 'promedio':8.22}
alumno10={'id':22, 'nombre':"Armando" , 'carrera':"ICO", 'promedio':7.32}

bd = []
bd.append(alumno1)
bd.append(alumno2)
bd.append(alumno3)
bd.append(alumno4)
bd.append(alumno5)
bd.append(alumno6)
bd.append(alumno7)
bd.append(alumno8)
bd.append(alumno9)
bd.append(alumno10)


verify_student(2, bd)


