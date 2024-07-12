"""Provides integer Binary Search Tree."""

from __future__ import annotations


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