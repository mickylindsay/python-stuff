"""Provides Stack data structure."""

from typing import Generic, TypeVar

from python_stuff.linked_list import LinkedList

T = TypeVar("T")


class Stack(Generic[T]):
    """Stack data structure implemented with singly linked list."""

    def __init__(self) -> None:
        """Creates an empty Stack."""
        self.head: LinkedList[T] | None = None

    def push(self, data: T) -> None:
        """Pushes new data onto the Stack."""
        self.head = LinkedList(data, self.head)

    def pop(self) -> T:
        """Pops top of the Stack and returns the data."""
        if self.head is None:
            msg = "Stack is empty"
            raise IndexError(msg)
        node = self.head
        self.head = self.head.next_
        return node.data

    def peek(self) -> T | None:
        """Returns data from to of the Stack."""
        if self.head is None:
            return None
        return self.head.data

    def length(self) -> int:
        """Returns number of items on stack."""
        if self.head is None:
            return 0
        return self.head.length()
