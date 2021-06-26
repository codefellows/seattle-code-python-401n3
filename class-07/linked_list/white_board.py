# PD: Write a function that takes a linke_list of letters, and return a string of the letters.

# Edge Cases
# Empty List - NO
# Always single letters

# Input output
# input: linked_list
# output: string

# Visual
# [p] -> [y] -> [t] -> [h] -> [o] -> [n] -> None
# Expect 'python'

# Big O
# Time o(n)
# Space o(1)

# Algo
# define function that takes in my lined_list
# create a variable to store my return value
# set the linked_list head to a current value
# traverse through the linked list with a while loop (current is not none) and concat the .value to my return variable
# return the return variabe

# code

def concat_ll(ll):
    stored_value = ''
    current = ll.head # p
    while current is not None:
        stored_value += current.value
        current = current.next
    return stored_value


# Test
# ll: [p] -> [y] -> [t] -> [h] -> [o] -> [n] -> None
#                                                ^
# stored_value = 'python'
