
number = 10

def recursive_count(num):
    if num > 0:
        print(num)
        recursive_count(num-1)


recursive_count(number)
