from estruturas.linked_list.linked_list import LinkedList


def test_append():
    linked_list = LinkedList()

    linked_list.append("A")
    linked_list.append("B")

    assert linked_list.head.data == "A"
    assert linked_list.head.next.data == "B"


def test_prepend():
    linked_list = LinkedList()

    linked_list.append("B")
    linked_list.prepend("A")

    assert linked_list.head.data == "A"
    assert linked_list.head.next.data == "B"


def test_find_existing_node():
    linked_list = LinkedList()

    linked_list.append("Python")
    linked_list.append("Java")

    node = linked_list.find("Java")

    assert node is not None
    assert node.data == "Java"


def test_find_non_existing_node():
    linked_list = LinkedList()

    linked_list.append("Python")

    assert linked_list.find("C#") is None


def test_remove_middle_node():
    linked_list = LinkedList()

    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")

    assert linked_list.remove("B") is True

    assert linked_list.find("B") is None
    assert len(linked_list) == 2


def test_remove_head():
    linked_list = LinkedList()

    linked_list.append("A")
    linked_list.append("B")

    assert linked_list.remove("A") is True

    assert linked_list.head.data == "B"
    assert len(linked_list) == 1


def test_remove_non_existing_node():
    linked_list = LinkedList()

    linked_list.append("Python")

    assert linked_list.remove("Java") is False


def test_len():
    linked_list = LinkedList()

    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")

    assert len(linked_list) == 3