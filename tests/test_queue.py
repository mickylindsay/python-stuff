from python_stuff.queue import Queue


def test_queue() -> None:
    queue = Queue[float]()
    queue.offer(1.2)
    queue.offer(1.3)
    queue.offer(1.4)
    queue.offer(1.5)
    queue.offer(1.6)
    assert queue.length() == 5
    assert queue.poll() == 1.2
    assert queue.length() == 4
    assert queue.peek() == 1.3
    assert queue.poll() == 1.3
    queue.offer(2.0)
    assert queue.poll() == 1.4
    assert queue.poll() == 1.5
    assert queue.length() == 2


def test_queue_pop_empty() -> None:
    assert Queue[int]().poll() is None


def test_queue_peek_empty() -> None:
    assert Queue[int]().peek() is None


def test_queue_length_empty() -> None:
    assert Queue[float]().length() == 0
