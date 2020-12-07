
import math
new_list = [1, 2, 3, 4, 5, 6, 7]

searched = 7

def recursive_bs(list, sear):
    
    mid = len(list)/2
    
    if sear == list[ int( math.floor( mid ) ) ]:
        print(f'ahuevo es { sear }')
    
    elif sear < list[ int( math.floor( mid ) ) ]:
        recursive_bs( list[ 0:int( math.floor( mid ) ) ], sear )
    elif sear > list[ int( math.floor( mid ) ) ]:
        recursive_bs( list[ int( math.floor( mid ) ):len(list) ], sear )

recursive_bs(new_list, searched)


