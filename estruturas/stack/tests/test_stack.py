from estruturas.stack.stack import Stack


def test_new_stack_is_empty():
    stack = Stack()

    assert stack.is_empty() is True


def test_push_adds_item_to_top():
    stack = Stack()

    stack.push("page-a")

    assert stack.peek() == "page-a"


def test_pop_removes_last_item():
    stack = Stack()
    stack.push("page-a")
    stack.push("page-b")

    removed_item = stack.pop()

    assert removed_item == "page-b"
    assert stack.peek() == "page-a"


def test_size_returns_number_of_items():
    stack = Stack()
    stack.push("page-a")
    stack.push("page-b")

    assert stack.size() == 2


def test_peek_returns_none_when_stack_is_empty():
    stack = Stack()

    assert stack.peek() is None


def test_pop_returns_none_when_stack_is_empty():
    stack = Stack()

    assert stack.pop() is None


def test_stack_is_not_empty_after_push():
    stack = Stack()

    stack.push("page-a")

    assert stack.is_empty() is False
