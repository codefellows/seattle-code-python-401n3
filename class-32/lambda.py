# def this_function(x):
#     return x

# hello = lambda x: x


# def sum_all(a, b, c):
#     return a +b +c

def which_is_larger(a, b):
    if a > b:
        return a
    else:
        return b


# print(which_is_larger(20, 40))


larger = lambda a, b: a if a > b else b

print(larger(40,20))
print(larger(100,12))

# sum = lambda a, b, c: a + b + c




# print(this_function('Hello'))

# print(hello())

# print(sum_all(2, 3, 5))

# print(sum(2, 3, 5))