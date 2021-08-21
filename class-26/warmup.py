def reverse1(lst):
    lst.reverse()
    return lst

def reverse2(lst):
    return [element for element in reversed(lst)]

def reverse3(lst):
    new_lst = lst[::-1]
    lst = new_lst
    return lst

def reverse4(lst):
    left = 0
    right = len(list)-1

    while left < right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        left += 1
        right += 1
    return lst



def reverse5(list):
    new