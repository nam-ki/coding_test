def solution(n, t):

    answer = n*(2**t)

    # answer = n<<t #=n * 2^t와 같은 결과값을 가진다.

    return answer

n=7
t=15

result = solution(n,t)

print(result)