def recursive(num):
    """ 
    The function will do a recursive call
    and return the the factorial sum of
    num.
    """
    if num <= 1:
        return 1

    print(num)
    return num + recursive(num - 1)
#   return num = recursive(recursive(recursive(recursive(recursive(1)))))

# recursive(5)
# 5 + 4 + 3 + 2 + 1 + 0

# return 5 + recursive(4) 15
    # return 4 + recursive(3) 10
        # return 3 + recursive(2) 6
            # return 2 + recursive(1) 1
                # return 1 

print(recursive(100))