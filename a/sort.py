from ds.binheap import PriorityQueue


def heapsort[T](arr: list[T]):
    pq = PriorityQueue()
    for val in arr:
        pq.push((val, val))

    for i in range(len(arr)):
        arr[i] = pq.pop()
