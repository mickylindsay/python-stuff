import pytest

from python_stuff.stack import Stack


def test_stack() -> None:
    stack = Stack[float]()
    stack.push(1.2)
    stack.push(1.3)
    stack.push(1.4)
    stack.push(1.5)
    stack.push(1.6)
    assert stack.length() == 5
    assert stack.pop() == 1.6
    assert stack.length() == 4
    assert stack.peek() == 1.5
    assert stack.pop() == 1.5
    stack.push(2.0)
    assert stack.pop() == 2.0
    assert stack.pop() == 1.4
    assert stack.length() == 2


def test_stack_pop_empty() -> None:
    with pytest.raises(IndexError, match="Stack is empty"):
        Stack[str]().pop()


def test_stack_peek_empty() -> None:
    assert Stack[int]().peek() is None


def test_stack_length_empty() -> None:
    assert Stack[float]().length() == 0
