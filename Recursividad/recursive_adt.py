import math

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

another_list = []

another_list.append(list.pop(0))

print(list)
print(another_list)

print(len(another_list)/2)
print(math.floor(0.5))

another_list.append(list.pop(0))
print(list)
print(another_list)
print(len(another_list)/2)
print(another_list[int((len(another_list)/2)-1)], another_list[int((len(another_list)/2))])

print( len(list) == 0 )
