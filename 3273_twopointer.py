import sys

n = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

arr.sort()
start, end =0, n-1
ans =0

while start < end:
    tmp = arr[start] + arr[end]
    if(tmp == x):
        ans +=1
        start +=1
    elif tmp < x:
        start +=1
    else: end -=1

print(ans)