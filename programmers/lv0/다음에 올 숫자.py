def solution(common):
    answer = 0

    common_len = len(common)

    #등차수열
    if (common[1] - common[0]) == (common[2] - common[1]):
        dif = common[1] - common[0]
        answer = common[common_len-1] + dif

    #등비수열
    elif (common[1] // common[0]) == (common[2] // common[1]):
        dif = common[1] // common[0]
        answer = common[common_len-1] * dif

    return answer

common = [4,12,36]

result = solution(common)

print(result)