import time
import random
from a import sort

random_integers = [random.randint(1, 10000) for _ in range(10000)]

sorts = {
    "bubble": sort.bubble_sort,
    "selection": sort.selection_sort,
    "insertion": sort.insertion_sort,
    "merge": sort.merge_sort,
    "heap": sort.heap_sort,
    "hashed heap": sort.hashed_heap_sort,
    "heap (with heapq)": sort.heapq_heap_sort,
    "quick": sort.quick_sort,
    "python builtin sort": list.sort,
}

times = []

for alg in sorts:
    arr = random_integers.copy()
    s = time.process_time()
    if alg == "merge":  # not in-place
        arr = sorts[alg](arr)
    else:
        sorts[alg](arr)
    f = time.process_time()

    correct = True
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            correct = False
            break

    print(f"sorting by {alg}: {f - s}s {'✅' if correct else '❌'}")

    times.append((f - s, alg))

times.sort(key=lambda x: x[0])

print("\n=== ORDER OF FASTEST TIMES ===")
for i in range(len(times)):
    el_t, alg = times[i]
    print(f"{i + 1}. {alg}: {el_t}s")
