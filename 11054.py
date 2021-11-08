n = int(input())

arr = list(map(int, input().split()))

dpinc = [0 for i in range(n)]
dpdec = [0 for i in range(n)]
dp  = [0 for i in range(n)]


for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dpinc[i] < dpinc[j]:
            dpinc[i] = dpinc[j]
    dpinc[i] +=1


for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j] and dpdec[i] < dpdec[j]:
            dpdec[i] = dpdec[j]
    dpdec[i] +=1

for i in range(n):
    dp[i] = dpinc[i] + dpdec[i] -1

print(max(dp))
print(dpinc)
print(dpdec)