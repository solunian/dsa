from ds.bst import BSTSet

s = BSTSet[int]()

for i in range(10):
    s.add(i)


print(s)
print(10 in s, 6 in s, 1 in s, 5 in s)

s.remove(5)
print(s)

print(5 in s)
s.remove(8)
s.remove(0)

print(s)

s.remove(5)
