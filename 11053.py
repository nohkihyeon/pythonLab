# 가장 긴 증가하는 부분 수열
n = int(input())

arr = list(map(int, input().split()))

dp = [0 for i in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] +=1

print(max(dp))
