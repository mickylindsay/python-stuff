"""Provides HashTable data structure."""

from typing import Generic, TypeVar

from python_stuff.linked_list import LinkedList

K = TypeVar("K")
V = TypeVar("V")


class HashTable(Generic[K, V]):
    """HashTable data structure implemented with singly linked lists."""

    def __init__(self) -> None:
        """Creates an empty Queue."""
        self._capacity = 16
        self._count = 0
        self._buckets: list[LinkedList[tuple[K, V]] | None] = [None] * self._capacity

    def get(self, key: K) -> V | None:
        """Get data from hashtable with provided key."""
        hash_index = hash(key) % self._capacity
        node = self._buckets[hash_index]
        if node is None:
            return None
        if node.data[0] == key:
            return node.data[1]
        while node.next_ and node.next_.data[0] != key:
            node = node.next_
        if node.next_ is None:
            return None
        return node.next_.data[1]

    def put(self, key: K, value: V) -> None:
        """Put data it hashtable with provided key. Replaces duplicate key."""
        hash_index = hash(key) % self._capacity
        node = self._buckets[hash_index]
        if node is None:
            self._buckets[hash_index] = LinkedList((key, value))
            self._count += 1
            return
        if node.data[0] == key:
            self._buckets[hash_index] = LinkedList((key, value), node.next_)
            return
        while node.next_ and node.next_.data[0] != key:
            node = node.next_
        if node.next_ is None:
            node.next_ = LinkedList((key, value))
            self._count += 1
        else:
            replacement = LinkedList((key, value), node.next_.next_)
            node.next_ = replacement

    def remove(self, key: K) -> V | None:
        """Removes data by key and returns data. None if not found."""
        hash_index = hash(key) % self._capacity
        node = self._buckets[hash_index]
        if node is None:
            return None
        if node.data[0] == key:
            self._buckets[hash_index] = node.next_
            self._count -= 1
            return node.data[1]
        while node.next_ and node.next_.data[0] != key:
            node = node.next_
        if node.next_ is None:
            return None
        data = node.next_.data[1]
        node.next_ = node.next_.next_
        self._count -= 1
        return data

    def size(self) -> int:
        """Returns number of elements in hashtable."""
        return self._count


test = HashTable[str, str]()
