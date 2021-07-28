"""
given a binary tree, where the value of each node is a linked_list, where the value of each linked_list is a value of a list, write a function that will return the following in a tuple.  Sum of all list values, the largest value, the smallest value, and the value furthest removed from 0
"""

def function(BinaryTree):
    queue = Queue()
    sum = 0
    min = BinaryTree.root.value.head.value[0]
    max = BinaryTree.root.value.head.value[0]
    absolute = 0
    queue.enqueue(BinaryTree.root)
    # ----------- Binary Tree ------------
    while queue.peek():
        front = queue.dequeue()
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)
# ------------- Linked List ------------
        current = front.value.head
        while current is not None:
            # ----- list -----------
            for number in current.value:
                if number > max:
                    max = number
                if number < min:
                    min = number
                if abs(number) > absolute:
                    absolute = number
                sum += number
            current = current.next
    return (sum, min, max, absolute) 