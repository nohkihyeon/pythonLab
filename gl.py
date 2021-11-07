def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


print(solution(36, 3))
print(solution(120, 3))
print(solution(278, 3))
print(solution(19424, 3))
print(solution(10492831, 3))