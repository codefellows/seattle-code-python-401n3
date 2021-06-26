from linked_list import LinkedList, Node

def test_new_ll():
    ll = LinkedList()
    assert ll

def test_nodes():
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
    assert ll.head.value == 'p'
    assert ll.head.next.value == 'y'
    assert ll.head.next.next.value == 't'
    assert ll.head.next.next.next.value == 'h'
    assert ll.head.next.next.next.next.value == 'o'
    assert ll.head.next.next.next.next.next.value == 'n'

# p -> y -> t -> h -> o -> n

def test_nodes_output():
    ll = LinkedList()
    node1 = Node('h')
    node2 = Node('y')
    node3 = Node('n')
    node4 = Node('t')
    node5 = Node('p')    
    node6 = Node('o')
    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    assert str(ll) != 'p -> y -> t -> h -> o -> n -> None'
    assert str(ll) == 'h -> y -> n -> t -> p -> o -> None'
