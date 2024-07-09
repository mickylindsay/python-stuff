"""Provides LinkedList data structure."""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class LinkedList(Generic[T]):
    """Singly-linked list structure."""

    def __init__(self, data: T, next_: Optional["LinkedList[T]"] = None) -> None:
        """Creates an empty LinkedList with None head."""
        self.data = data
        self.next_ = next_

    def add(self, data: T) -> "LinkedList[T]":
        """Appends new data to end of LinkedList."""
        cur = self
        while cur.next_:
            cur = cur.next_
        cur.next_ = LinkedList(data)
        return cur.next_

    def _traverse(self, num: int) -> "LinkedList[T]":
        cur = self
        i = num
        while i > 0:
            if cur.next_ is None:
                msg = "index out of range"
                raise IndexError(msg)
            cur = cur.next_
            i -= 1
        return cur

    def insert(self, index: int, data: T) -> "LinkedList[T]":
        """Inserts new value into LinkedList at provided index."""
        if index <= 0:
            msg = "index must be greater than 0"
            raise ValueError(msg)
        cur = self._traverse(index - 1)
        node = LinkedList(data)
        node.next_ = cur.next_
        cur.next_ = node
        return node

    def remove(self, index: int) -> T:
        """Removes new value from LinkedList at provided index and returns it."""
        if index <= 0:
            msg = "index must be greater than 0"
            raise ValueError(msg)
        cur = self._traverse(index - 1)
        node = cur.next_
        if node is None:
            msg = "index out of range"
            raise IndexError(msg)
        cur.next_ = node.next_
        return node.data

    def get(self, index: int) -> T:
        """Get data from list at provided index."""
        if index < 0:
            msg = "index must be greater than 0"
            raise ValueError(msg)
        return self._traverse(index).data

    def length(self) -> int:
        """Returns length of LinkedList."""
        cur = self
        count = 1
        while cur.next_:
            cur = cur.next_
            count += 1
        return count
