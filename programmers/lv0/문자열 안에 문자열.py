def solution(str1, str2):

    if str2 in str1:
        answer = 1
    else:
        answer = 2

    return answer

str1 = "ppprrrogrammers"
str2 = "pppp"

result = solution(str1,str2)

print(result)