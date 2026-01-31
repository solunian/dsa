from lib.generics import Comparable, Hashable

# min binheap representation
# parent(i) = (i - 1) // 2
# left(i) = i * 2 + 1, right(i) = i * 2 + 2


# NORMAL PRIORITY QUEUE: no decrease/increase key operation
# simply add the value again into the queue with the new priority
class PriorityQueue[T: Comparable]:
    def _heapify_up(self, i: int):
        while i > 0:
            parent_i = (i - 1) // 2
            if self._arr[i] < self._arr[parent_i]:
                # swap, update i
                self._arr[i], self._arr[parent_i] = self._arr[parent_i], self._arr[i]
                i = parent_i
            else:
                break

    def _heapify_down(self, i: int):
        while True:
            smallest = i
            li, ri = i * 2 + 1, i * 2 + 2

            # bounds check and min-property check
            if li < len(self._arr) and self._arr[li] < self._arr[i]:
                smallest = li

            if ri < len(self._arr) and self._arr[ri] < self._arr[smallest]:
                smallest = ri

            # neither one was smaller
            if smallest == i:
                break

            # swap smallest with parent
            self._arr[i], self._arr[smallest] = self._arr[smallest], self._arr[i]

            i = smallest

    def __init__(self):
        self._arr: list[T] = []

    def __len__(self) -> int:
        return len(self._arr)

    def __str__(self) -> str:
        return str(self._arr)

    def push(self, x: T):
        self._arr.append(x)

        # bubble up
        self._heapify_up(len(self._arr) - 1)

    def peek(self) -> T:
        if len(self._arr) == 0:
            raise IndexError("peek on empty list")

        return self._arr[0]

    def pop(self) -> T:
        if len(self._arr) == 0:
            raise IndexError("pop on empty list")

        popped = self._arr[0]

        if len(self._arr) == 1:
            self._arr.clear()
            return popped

        # bubble down
        self._arr[0] = self._arr.pop()
        self._heapify_down(0)

        return popped


# HASHED PRIORITY QUEUE: for O(1) decrease/increase key operation
# duplicates values will mess with update_key
class HashedPriorityQueue[K: Comparable, V: Hashable]:
    def _heapify_up(self, i: int):
        while i > 0:
            parent_i = (i - 1) // 2
            if self._arr[i][0] < self._arr[parent_i][0]:
                # swap, update i
                self._arr[i], self._arr[parent_i] = self._arr[parent_i], self._arr[i]

                # update index_map
                self._index_map[self._arr[parent_i][1]] = parent_i
                self._index_map[self._arr[i][1]] = i

                i = parent_i
            else:
                break

    def _heapify_down(self, i: int):
        while True:
            smallest = i
            li, ri = i * 2 + 1, i * 2 + 2

            # bounds check and min-property check
            if li < len(self._arr) and self._arr[li][0] < self._arr[i][0]:
                smallest = li

            if ri < len(self._arr) and self._arr[ri][0] < self._arr[smallest][0]:
                smallest = ri

            # neither one was smaller
            if smallest == i:
                break

            # swap smallest with parent
            self._arr[i], self._arr[smallest] = self._arr[smallest], self._arr[i]

            # set index map
            self._index_map[self._arr[i][1]] = i
            self._index_map[self._arr[smallest][1]] = smallest

            i = smallest

    def __init__(self):
        # (priority, value)
        self._arr: list[tuple[K, V]] = []
        self._index_map: dict[V, int] = {}

    def __len__(self) -> int:
        return len(self._arr)

    def __str__(self) -> str:
        return str(self._arr) + "\n" + str(self._index_map)

    def push(self, k: K, v: V):
        # if x[1] in self._index_map:
        #     raise KeyError("cannot push duplicate")

        self._arr.append((k, v))
        self._index_map[v] = len(self._arr) - 1

        # bubble up
        self._heapify_up(len(self._arr) - 1)

    def peek(self) -> V:
        if len(self._arr) == 0:
            raise IndexError("peek on empty list")

        return self._arr[0][1]

    def pop(self) -> V:
        if len(self._arr) == 0:
            raise IndexError("pop on empty list")

        popped = self._arr[0][1]

        # in case duplicate values messing with update_key
        if popped in self._index_map:
            del self._index_map[popped]

        if len(self._arr) == 1:
            self._arr.clear()
            return popped

        # bubble down
        self._arr[0] = self._arr.pop()
        self._heapify_down(0)

        return popped

    # decrease/increase key
    def update_key(self, v: V, new_key: K):
        if v not in self._index_map:
            raise KeyError("item x does not exist")

        i = self._index_map[v]
        old_key = self._arr[i][0]

        if new_key == old_key:
            return

        self._arr[i] = (new_key, v)
        if new_key < old_key:
            self._heapify_up(i)
        else:
            self._heapify_down(i)
