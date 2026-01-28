# O(2^n)
def bad_fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return bad_fib(n - 2) + bad_fib(n - 1)


# O(n)
def fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1

    i_2, i_1, i = 0, 1, 1  # starting seq
    for _ in range(2, n + 1):
        i = i_2 + i_1
        i_2, i_1 = i_1, i  # set for next calc
    return i


# ~O(1), becomes inaccurate for n >= ~72. apparently
def binet(n: int) -> int:
    gr = (1 + 5**0.5) / 2
    conj = (1 + 5**0.5) / 2

    # return round(gr**n / (5**0.5))
    return round((gr**n - conj**n) / (5**0.5))
