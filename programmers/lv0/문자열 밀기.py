# def solution(A,B):
#     answer = 0
#
#     for i in range(len(A)):
#         if B == A:
#             break
#         C=list(A)
#         last_char = C[len(A)-1]
#         for j in range(len(A)-1,0,-1):
#             C[j] = C[j-1]
#         C[0] = last_char
#         A=''.join(C)
#         answer += 1
#         if answer == len(A):
#             answer = -1
#
#     return answer

# def solution(A,B):
#     answer = 0
#
#     for i in range(len(A)):
#         if B == A:
#             break
#
#         last_char = A[-1]
#         A = last_char+A[:-1]
#         answer += 1
#         if answer == len(A):
#             answer = -1
#
#     return answer

def solution(A,B):
    answer = (B*2).find(A)

    return answer

A="apple"
B="eappl"

result = solution(A,B)

print(result)