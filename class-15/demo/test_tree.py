@pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


@pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


@pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


@pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree


@pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None


@pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree