from lib.generics import Comparable


def count_inversions[T: Comparable](arr: list[T]) -> tuple[list[T], int]:
    def merge(arr1: list[T], arr2: list[T]) -> tuple[list[T], int]:
        c = 0
        res = []

        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                c += len(arr1) - i
                j += 1

        if i < len(arr1):
            res += arr1[i:]

        if j < len(arr2):
            res += arr2[j:]

        return res, c

    if len(arr) <= 1:
        return arr, 0
    if len(arr) == 2:
        return (arr, 0) if arr[0] <= arr[1] else ([arr[1], arr[0]], 1)

    left, right = arr[: len(arr) // 2], arr[len(arr) // 2 :]

    lres, lc = count_inversions(left)
    rres, rc = count_inversions(right)
    res, mc = merge(lres, rres)

    return res, lc + rc + mc
