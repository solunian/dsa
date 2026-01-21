from ds.linkedlist import LinkedList

ll = LinkedList[int]()

for i in range(10):
    ll.append(i)


print(ll[6])
print(ll[-10])

for i in ll:
    print(i, end=" ")

print(10 in ll, 9 in ll)


del ll[-1]
del ll[5]
del ll[0]

print(ll)


ll2 = LinkedList[int]()
for i in range(10, 1000, 25):
    ll2.append(i)

ll += ll2

print(ll)
print(ll2)

llist = LinkedList[int]()

llist.insert(0, 0)
llist.insert(0, 100)
llist.insert(1, 1000)
llist.insert(2, 700)
llist.insert(0, 10)
llist.insert(len(llist) - 1, 100)
llist.insert(100, 69420)

del llist[3]

print(llist)
print(llist.index(69420), llist.index(100))
