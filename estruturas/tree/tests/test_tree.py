from estruturas.tree.tree import BinarySearchTree


def test_empty_tree():
    tree = BinarySearchTree()

    assert tree.root is None
    assert tree.search(50) is False
    assert tree.find_min() is None
    assert tree.find_max() is None
    assert tree.in_order() == []


def test_insert_root():
    tree = BinarySearchTree()

    tree.insert(50)

    assert tree.root is not None
    assert tree.root.data == 50


def test_insert_left_and_right_nodes():
    tree = BinarySearchTree()

    tree.insert(50)
    tree.insert(30)
    tree.insert(70)

    assert tree.root.left is not None
    assert tree.root.left.data == 30

    assert tree.root.right is not None
    assert tree.root.right.data == 70


def test_search_existing_value():
    tree = BinarySearchTree()

    tree.insert(50)
    tree.insert(30)
    tree.insert(70)

    assert tree.search(30) is True
    assert tree.search(70) is True


def test_search_missing_value():
    tree = BinarySearchTree()

    tree.insert(50)
    tree.insert(30)
    tree.insert(70)

    assert tree.search(100) is False


def test_find_min_and_max():
    tree = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

    assert tree.find_min() == 20
    assert tree.find_max() == 80


def test_in_order_returns_sorted_values():
    tree = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

    assert tree.in_order() == [20, 30, 40, 50, 60, 70, 80]


def test_duplicate_values_are_ignored():
    tree = BinarySearchTree()

    values = [50, 30, 70, 30, 50, 70]

    for value in values:
        tree.insert(value)

    assert tree.in_order() == [30, 50, 70]