class Node:
  def __init__(self, value = None, next = None):
    self.next = next
    self.value = value

class LinkedList:

  def __init__(self):
    self.head = None


  def add(self, value):
    node = Node(value)

    if self.head is None:
      self.head = node
      return

    current = self.head
    while current.next is not None:
      current = current.next

    current.next = node

  def get_max_iteratively(self):
    largest = 0
    current = self.head
    while current is not None:
      if current.value > largest:
        largest = current.value
      current = current.next
    return largest

  def get_max_recursively(self):
    
    def get_max(node, largest=0):
      if node is None:
        return largest
      if node.value > largest:
        largest = node.value
      return get_max(node.next, largest)
    
    return get_max(self.head)


if __name__ == "__main__":
  ll = LinkedList()
  ll.add(7)
  ll.add(2)
  ll.add(13)
  ll.add(9)
  ll.add(3)
  print(ll.get_max_iteratively())

  ll1 = LinkedList()
  ll1.add(7)
  ll1.add(2)
  ll1.add(88)
  ll1.add(9)
  ll1.add(3)
  print(ll1.get_max_recursively())