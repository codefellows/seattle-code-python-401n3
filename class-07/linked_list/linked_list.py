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

if __name__ == "__main__":
    ll = LinkedList()
    node1 = Node('p')
    node2 = Node('y')
    node3 = Node('t')
    node4 = Node('h')
    node5 = Node('o')    
    node6 = Node('n')
    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6