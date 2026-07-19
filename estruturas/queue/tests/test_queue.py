from estruturas.queue.queue_structure import Queue


def test_enqueue_increases_queue_length():
    queue = Queue()

    queue.enqueue("CX-1001")

    assert len(queue) == 1


def test_dequeue_removes_first_item():
    queue = Queue()

    queue.enqueue("CX-1001")
    queue.enqueue("CX-1002")
    queue.enqueue("CX-1003")

    removed_item = queue.dequeue()

    assert removed_item == "CX-1001"
    assert len(queue) == 2


def test_dequeue_on_empty_queue():
    queue = Queue()

    assert queue.dequeue() is None


def test_peek_returns_first_item():
    queue = Queue()

    queue.enqueue("CX-1001")
    queue.enqueue("CX-1002")

    assert queue.peek() == "CX-1001"
    assert len(queue) == 2


def test_peek_on_empty_queue():
    queue = Queue()

    assert queue.peek() is None


def test_new_queue_is_empty():
    queue = Queue()

    assert queue.is_empty() is True


def test_queue_with_items_is_not_empty():
    queue = Queue()

    queue.enqueue("CX-1001")

    assert queue.is_empty() is False


def test_queue_follows_fifo_order():
    queue = Queue()

    queue.enqueue("CX-1001")
    queue.enqueue("CX-1002")
    queue.enqueue("CX-1003")

    assert queue.dequeue() == "CX-1001"
    assert queue.dequeue() == "CX-1002"
    assert queue.dequeue() == "CX-1003"

