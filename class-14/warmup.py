# Given a linked_list, where the values are lists, find the highest int.

# create the function takes the ll
# create a variable to store the highest value
# create a variable to traverse through the ll
# traverse through the ll.
# at each node, iterate throught the list and compare to the highest value
# return the highest value

def get_highest_value_iter(ll):
    highest_value = 0
    current = ll.head
    while current:
        # do something to the ll
        # current.value []
        for i in current.value:
            if i > highest_value:
                highest_value =i
        current = current.next
    return highest_value

def get_highest_value_recur(ll):
    current = ll.head

    def walk(node, highest_value = 0):
        if node is None:
            return highest_value

        for i in node.value:
            if i > highest_value:
                highest_value = i

        return walk(node.next, highest_value)
    return walk(current)


# [1, 2, 3] -> [2, 4, 1] -> [9] -> None