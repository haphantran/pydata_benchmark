from contextlib import contextmanager
from time import perf_counter, sleep
from functools import lru_cache
output = []
@contextmanager
def timer(msg):
    start = perf_counter()
    try:
      yield
    finally:
      end = perf_counter()
      print(f"{msg:<24}Elapsed time: \N{mathematical bold capital delta}t = {end - start:.6f}")
      output.append((msg, end - start))


from random import randint as py_randint
from numpy.random import randint as np_randint
from numpy import dot as np_dot

SIZE = 1_000_000

with timer('python list: create'):
  py_xs = [py_randint(0, SIZE) for _ in range(SIZE)]
  py_ys = [py_randint(0, SIZE) for _ in range(SIZE)]

with timer('np create'):
  np_xs = np_randint(0, SIZE, SIZE)
  np_ys = np_randint(0, SIZE, SIZE)





fib_SIZE = 10000
@lru_cache(maxsize=5)
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

with timer('fibonacci'):
  fibonacci(fib_SIZE)

print(output)