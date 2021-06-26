class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next



class LinkedList:

    def init__(self, head=None):
        self.head = head
    
    def __str__(self):
        output = ''
        current = self.head
        while current:
            output += f'{current.value} -> '
            current = current.next
        return output + 'None'