import time
import a.fibonacci as fib

s = time.process_time()
for i in range(1000):
    fib.fib(i)
f = time.process_time()
print(f - s)

print(fib.fib(100))
