"""Provides Queue data structure."""

from typing import Generic, TypeVar

from python_stuff.linked_list import LinkedList

T = TypeVar("T")


class Queue(Generic[T]):
    """Queue data structure implemented with singly linked list."""

    def __init__(self) -> None:
        """Creates an empty Queue."""
        self.head: LinkedList[T] | None = None
        self.tail: LinkedList[T] | None = None

    def offer(self, data: T) -> None:
        """Adds data to queue."""
        if self.head is not None:
            self.tail = self.head.add(data)
        else:
            node = LinkedList(data)
            self.head = node
            self.tail = node

    def poll(self) -> T | None:
        """Removes the first element in Queue and returns the data."""
        if self.head is None:
            return None
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
