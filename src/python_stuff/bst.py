"""Provides integer Binary Search Tree."""

from __future__ import annotations
from typing import Callable


class BST:
    """BST data structure."""

    def __init__(self, data: int) -> None:
        """Creates a BST node with provided value and no children."""
        self.value = data
        self.left: BST | None = None
        self.right: BST | None = None

    def insert(self, data: int) -> BST:
        """Insert new BST node into tree."""
        if self.value == data:
            return self
        if self.value < data:
            if self.right:
                return self.right.insert(data)
            self.right = BST(data)
            return self.right
        if self.left:
            return self.left.insert(data)
        self.left = BST(data)
        return self.left

    def search(self, data: int) -> BST | None:
        """Search and return BST node with input value. None if not found."""
        if self.value == data:
            return self
        if self.value < data and self.right:
            return self.right.search(data)
        if self.value > data and self.left:
            return self.left.search(data)
        return None

    def delete(self, data: int) -> BST | None:
        if self.value == data:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # navigate to successor (furthest left child of right subtree)
            node = self.right
            prev = node
            while node.left:
                prev = node
                node = node.left
            prev.left = None
            self.value = node.value
        elif self.value < data and self.right:
            self.right = self.right.delete(data)
        elif self.value > data and self.left:
            self.left = self.left.delete(data)
        return self

def traverse_in_order(bst: BST | None, fn: Callable[[BST], None]) -> None:
    if bst is None:
        return
    traverse_in_order(bst.left, fn)
    fn(bst)
    traverse_in_order(bst.right, fn)