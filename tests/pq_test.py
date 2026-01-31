from ds.binheap import HashedPriorityQueue

pq = HashedPriorityQueue[int, str]()
pq.push(5, "one")
print(pq)
pq.push(2, "two")
print(pq)
pq.push(3, "three")
print(pq)

pq.push(4, "four")
print(pq)

pq.update_key("two", 6)
print(pq)

pq.push(10, "five")
pq.push(3, "six")
print(pq)

pq.push(8, "seven")
pq.push(9, "eight")
pq.push(5, "nine")

print(pq)

pq.update_key("nine", 1)
print(pq)


print("========")

for i in range(4):
    pq.pop()
    print(pq)
