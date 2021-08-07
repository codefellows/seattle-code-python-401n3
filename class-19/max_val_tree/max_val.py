def find_max_value(self):
    root_node = self.root

    if not root_node:
        raise ValueError('The Tree is Empty')
    max_value = root_node.value

    def find_max(node):
        if not node:
            return

        if node.left:
            if node.left.value > max_value:
                max_value = node.left.value

            find_max(node.left)

        if node.right:
            if node.right.value > max_value:
                max_value = node.right.value

            find_max(node.right)

        find_max(root_node)
        return max_value

# Test

def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.right = Node(30)
    tree.root.left = Node(7)

    actual = tree.find_max()
    expected = 30
    assert actual == expected