from lib.generics import Comparable
from collections import deque


class MinStack[T: Comparable]:
    def __init__(self):
        # [0]: element, [1]: min element so far
        self._stack = deque[tuple[T, T]]()

    def __len__(self) -> int:
        return len(self._stack)

    def __str__(self) -> str:
        return str(self._stack)

    def append(self, x: T):
        if len(self._stack) == 0:
            self._stack.append((x, x))
        else:
            curr_min = self._stack[-1][1]
            if x < curr_min:
                self._stack.append((x, x))
            else:
                self._stack.append((x, curr_min))

    def peek(self) -> T:
        if len(self._stack) == 0:
            raise IndexError("peek on empty stack")

        return self._stack[-1][0]

    def min(self) -> T:
        if len(self._stack) == 0:
            raise IndexError("min on empty stack")

        return self._stack[-1][1]

    def pop(self) -> T:
        if len(self._stack) == 0:
            raise IndexError("pop on empty stack")

        return self._stack.pop()[0]
