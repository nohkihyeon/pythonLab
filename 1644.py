N = int(input())

prime = [False, False] + [True] *(N-1)
primeArray = []

for i in range(2, N+1):
    if prime[i]:
        primeArray.append(i)
        for j in range(2*i, N+1, i):
            prime[j] = False


start = 0
end = 0
sum = 0
ans = 0

while end <= len(prime):
    tmp = sum(prime[start:end])
    if sum >= N:
        start +=1
    else:
        end += 1

    if sum == N:
        ans +=1

print(ans)