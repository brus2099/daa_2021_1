
new_list = [ 1, 2, 3, 4 ]

def recursive_add(list):

    if len(list) > 1:
        return list.pop() + recursive_add(list)
    elif len(list) == 1:
        return list[0]

print(recursive_add(new_list))

