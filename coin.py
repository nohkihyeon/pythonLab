N, K = map(int, input().split())
coin = []
for _ in range(N):
    value = int(input())
    if value <=K:
        coin.append(value)

ans = 0
for i in range(len(coin)):
    value = coin[len(coin) - i - 1]
    ans += K // value
    K %= value

print(ans)