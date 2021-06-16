def remove_dupes(old_list):
    '''
    Function to remove duplicates from a list and return a new list
    '''
    new_list = []
    for idx in old_list:
        if idx not in new_list:
            new_list.append(idx)

    return new_list

# Invoke the function
print(remove_dupes([1, 2, 1, 3, 2, 4]))
#                   ^

# Testing

# new_list = [1, 2, 3, 4, 5]
# 1, 2, 3, 4, 5