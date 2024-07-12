"""Provides string Rope data structure."""

from __future__ import annotations


class Rope:
    """Rope data structure."""

    def __init__(self) -> None:
        """Creates an empty string Rope."""
        self.data: str | None = None
        self.weight = 0
        self.left: Rope | None = None
        self.right: Rope | None = None

    def index(self, index: int) -> str:
        """Return the character at index i within the Rope."""
        if index < self.weight and self.left:
            return self.left.index(index)
        if self.right:
            return self.right.index(index - self.weight)
        if self.data:
            return self.data[index]
        raise ValueError

    def concat(self, other: Rope) -> Rope:
        """Concatenate two Ropes together. Returns combined Rope."""
        rope = Rope()
        rope.left = self
        rope.right = other
        weight = self.weight
        if self.right:
            weight += self.right.weight
        rope.weight = weight
        # balance if needed?
        return rope

    # I gotta write an AVS again or a splay tree or something to
    # remember all the zigzaging around to balance and splice a bst
    def split(self, index: int) -> Rope | None:
        """Splits the current rope at index. Modifies current rope and returns new separated rope section."""
        if index < self.weight and self.left:
            self.left.split(index)
            # Mutate self and return right side (right side is cut off part concat with right?)
            self.weight = index  # ?
            return None
        if index > self.weight and self.right:
            self.right.split(index - self.weight)
            # Mutate
            return None
        right = self.right
        self.right = None
        return right
