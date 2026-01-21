import random
from a.sort import heapsort

# Generate a list of 10 random integers between 1 and 100
random_integers = [random.randint(1, 20) for _ in range(10)]
print(random_integers)

heapsort(random_integers)

print(random_integers)


# l = [6, 10, 18, 8, 8, 12, 12, 2, 18, 9]

# heapsort(l)
# print(l)
