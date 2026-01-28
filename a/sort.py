from lib.generics import Comparable
from ds.binheap import PriorityQueue


# bubble largest up (sorted right first)
def bubble_sort[T: Comparable](arr: list[T]):
    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # end-early optimization for O(n) best case
        if not swapped:
            break


# select smallest to index i (sorted left first)
def selection_sort[T: Comparable](arr: list[T]):
    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]


# insert to the right (sorted left first)
def insertion_sort[T: Comparable](arr: list[T]):
    for i in range(len(arr)):
        tmp = arr[i]
        for j in range(i + 1, len(arr)):
            if tmp > arr[j]:
                arr[j - 1] = arr[j]
            else:
                arr[j] = tmp
                break


def merge_sort[T: Comparable](arr: list[T]) -> list[T]:
    def merge(arr1: list[T], arr2: list[T]) -> list[T]:
        res = []

        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        if i < len(arr1):
            res += arr1[i:]

        if j < len(arr2):
            res += arr2[j:]

        return res

    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        return arr if arr[0] <= arr[1] else [arr[1], arr[0]]

    left, right = arr[: len(arr) // 2], arr[len(arr) // 2 :]

    return merge(merge_sort(left), merge_sort(right))


def heap_sort[T: Comparable](arr: list[T]):
    pq = PriorityQueue()
    for val in arr:
        pq.push((val, val))

    for i in range(len(arr)):
        arr[i] = pq.pop()
