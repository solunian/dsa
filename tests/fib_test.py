import time
import a.fibonacci as fib

s = time.perf_counter()
for i in range(1000):
    fib.fib(i)
f = time.perf_counter()
print(f - s)

print(fib.fib(100))
