# def solution(my_str, n):
#     answer = []
#
#     while(1):
#         if len(my_str) <= n:
#             answer.append(my_str)
#             break
#         else:
#             answer.append(my_str[:n])
#             my_str = my_str[n:len(my_str)]
#
#     return answer

def solution(my_str, n):
    answer = []

    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])

    return answer

my_str = "abc1Addfggg4556b"
n=6

result = solution(my_str,n)

print(result)