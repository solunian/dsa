from ds.minstack import MinStack

a = MinStack[int]()
for i in [5, 6, 2, 1, 3, 6]:
    a.append(i)

print(a.pop())
print(a)
