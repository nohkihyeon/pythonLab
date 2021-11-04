import sys

n = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))

arr.sort()
start, end =0, n-1
ansStart, ansEnd =0, 0
min = sys.maxsize

while start < end:
    tmp = arr[start] + arr[end]
    if(min > abs(tmp)):
        ansStart = arr[start]
        ansEnd = arr[end]

    elif tmp <= 0:
        start +=1
    else: end -=1

print(ansStart, " ", ansEnd)