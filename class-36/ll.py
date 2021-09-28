#  ll = [2] -> [4] -> [6] -> None
#                      ^
# current ll.head


def sorted_ascending(ll):
   if not ll.head:
       return False
   current = ll.head
   while (current.next):
       if current.next.value < current.value:
           return False
       current = current.next
   return True
# Potential Solution Part 2

def sorted_either_direction(ll):
    if not ll.head:
        return False
    is_ascending = True
    is_descending = True
    current = ll.head
    while current.next and (is_ascending or is_descending):
        cv = current.value
        nv = current.next.value
        if nv < cv:
            is_ascending = False
        if nv > cv:
            is_descending = False
        current = current.next
    return is_ascending or is_descending