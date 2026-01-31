from ds.bst import BSTSet
import random

s = BSTSet[int]()

a = [2, 1, 4, 6, 3, 0, 5]
for i in range(len(a)):
    # rand = random.randint(0, 100)
    # print(f"inserted: {rand}")
    s.add(a[i])

print(s)

print(10 in s, 6 in s, 1 in s, 5 in s)

s.remove(5)
print(s)

s.remove(2)

print(s)

s.remove(3)
print(s)

s.remove(4)
print(s)

s.remove(6)
print(s)

s.remove(6)
