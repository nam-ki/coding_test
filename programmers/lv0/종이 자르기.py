def solution(M,N):
    answer = 0

    #M = 가로, N = 세로

    split_M = M-1
    split_N = N-1

    answer = split_M+M*split_N

    return answer

M=2
N=5

result = solution(M,N)

print(result)