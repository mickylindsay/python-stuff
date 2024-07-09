"""Provides LinkedList data structure."""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class LinkedList(Generic[T]):
    """Singly linked list structure."""

    def __init__(self, data: T, next_: Optional["LinkedList[T]"] = None) -> None:
        """Creates an empty LinkedList with None head."""
        self.data = data
        self.next_ = next_

    def add(self, data: T) -> None:
        """Appends new data to end of LinkedList."""
        cur = self
        while cur.next_:
            cur = cur.next_
        cur.next_ = LinkedList(data)

    def length(self) -> int:
        """Returns length of LinkedList."""
        cur = self
        count = 1
        while cur.next_:
            cur = cur.next_
            count += 1
        return count
