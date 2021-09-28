def get_largest(t):
 
   if not t.root:
       return 0
 
   def walk(tree_node, largest):
       if not tree_node:
           return largest
 
       current = tree_node.value.head
 
       while current:
           if abs(current.value) > abs(largest):
               largest = current.value
           current = current.next
 
       largest = walk(tree_node.left, largest)
        #         walk(left, 4)
        #         walk(None, 5)
       largest = walk(tree_node.right, largest)
        #         walk(right, 4)
 
       return largest
   return walk(t.root, 0)

#                  root [2] -> [3] -> [4] -> None
# Largest: -22
# left [2] -> [5] -> [3] -> None         right [-22] -> [8] -> [1] -> None
#  C                         ^

# Expected: -22