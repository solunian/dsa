from typing import Self


class Node[T]:
    def __init__(self, val: T, next: Self | None = None):
        self.val = val
        self.next = next


class DoublyNode[T]:
    def __init__(self, val: T, next: Self | None = None, prev: Self | None = None):
        self.val = val
        self.next = next
        self.prev = prev
