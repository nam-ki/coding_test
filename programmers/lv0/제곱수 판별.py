def solution(n):

    dec = n**(1/2)

    #제곱근 판별
    if dec - int(dec) == 0.0:
        answer = 1
    else:
        answer = 2
    return answer

n=976

result = solution(n)

print(result)