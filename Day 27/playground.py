def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

print(add(1,3,5,7,9))