from typing import Self


class Node[T]:
    def __init__(self, val: T, next: Self | None = None):
        self.val = val
        self.next = next

    def __iter__(self):
        yield self.val

        if self.next is not None:
            yield from self.next


class DoublyNode[T]:
    def __init__(self, val: T, next: Self | None = None, prev: Self | None = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __iter__(self):
        yield self.val

        if self.next is not None:
            yield from self.next


class BinaryNode[T]:
    def __init__(self, val: T, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right

    # pre-order iter!
    def __iter__(self):
        if self.left is not None:
            yield from self.left

        yield self.val

        if self.right is not None:
            yield from self.right
