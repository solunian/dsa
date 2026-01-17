from typing import Self
from lib.node import Node


class LinkedList[T]:
    def __init__(self):
        self._head: Node[T] | None = None
        self._tail: Node[T] | None = None
        self._len: int = 0

    def __len__(self) -> int:
        return self._len

    def __iadd__(self, other: Self) -> Self:
        self.extend(other)
        return self

    def __iter__(self):
        curr = self._head
        while curr is not None:
            yield curr.val
            curr = curr.next

    def __getitem__(self, i: int) -> T:
        if i < 0:  # negative indexing
            i = self._len + i

        if not (0 <= i < self._len):
            raise IndexError("index out of bounds")

        if i == self._len - 1:
            return self._tail.value  # type: ignore

        curr = iter(self)
        for _ in range(i - 1):
            next(curr)
        return next(curr)

    def __setitem__(self, i: int, value: T):
        if i < 0:  # negative indexing
            i = self._len + i

        if not (0 <= i < self._len):
            raise IndexError("index out of bounds")

        if i == self._len - 1:
            self._tail.value = value  # type: ignore
            return

        curr = self._head
        for _ in range(i):
            curr = curr.next  # type: ignore
        curr.value = value  # type: ignore

    def __delitem__(self, i: int):
        if i < 0:  # negative indexing
            i = self._len + i

        if not (0 <= i < self._len):
            raise IndexError("index out of bounds")

        if i == 0:
            if self._head is self._tail:
                self._head = self._tail = self._head.next  # type: ignore
            else:
                self._head = self._head.next  # type: ignore
        else:
            curr = self._head
            for _ in range(i - 1):
                curr = curr.next  # type: ignore

            # curr.next is to be deleted. if points to tail, tail = curr
            if curr.next is self._tail:  # type: ignore
                self._tail = curr
            curr.next = curr.next.next  # type: ignore

        self._len -= 1

    def __str__(self) -> str:
        return str(list(self))

    def append(self, x: T):
        if self._tail is None:
            self._head = self._tail = Node(x)
        else:
            self._tail.next = Node(x)
            self._tail = self._tail.next

        self._len += 1

    # self consumes other
    def extend(self, other: Self):
        if self._tail is None:
            self._head = other._head
            self._tail = other._tail
        else:
            self._tail.next = other._head
            if other._tail is not None:
                self._tail = other._tail

        other._head = None
        other._tail = None
        other._len = 0

        self._len += other._len

    # places item at the index of i. if i >= len, just appends
    def insert(self, i: int, x: T):
        if i < 0:  # negative indexing
            i = self._len + i

        if i < 0:
            raise IndexError("index out of bounds")
        if i >= self._len:
            self.append(x)
            return

        new_node = Node(x)

        if i == 0:
            new_node.next = self._head  # type: ignore
            self._head = new_node
        else:
            curr = self._head
            for _ in range(i - 1):
                curr = curr.next  # type: ignore

            new_node.next = curr.next  # type: ignore
            curr.next = new_node  # type: ignore

        self._len += 1

    def index(self, x: T) -> int:
        curr = self._head
        i = 0
        while curr is not None:
            if curr.val == x:
                return i
            curr = curr.next
            i += 1

        raise ValueError("item not found in linked list")
