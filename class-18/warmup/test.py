def post_order_traversal(tree, largest = 0):

    def walk(node, largest):
        if not node:
            return largest
        if node.left > largest:
            largest = node.left.value
            walk(node.left, largest)
        if node.right > largest:
            largest = node.right.value
            walk(node.right, largest)
        if node.value > largest:
            largest = node.value
    walk(tree.root, largest)

    # if tree.root is None:
    #     return largest
    # if tree.root.left is not None:
    #     if tree.left.value > largest:
    #         largest = tree.left.value
    #     post_order_traversal(tree.left, largest)
    # if tree.root.right is not None:
    #     if tree.right.value > largest:
    #         largest = tree.right.value
    #     post_order_traversal(tree.right, largest)
    # if tree.root.value > largest:
    #     largest = tree.root.value
    # return largest


    #     100
    #    /   \
    #   90   110
    #  /79 \   /  \
    #  99 105  115    

    # largest = 90