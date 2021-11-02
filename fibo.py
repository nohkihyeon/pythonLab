# Dynamic Programming

import time

d = [0] * 50

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

for num in range(5, 40, 10):
    start = time.time()
    res = fibo(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')


def fibo2(x):
    if x == 1 or x == 2:
        return 1

    return fibo2(x-1) + fibo2(x-2)

for num in range(5, 40, 10):
    start = time.time()
    res = fibo2(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')