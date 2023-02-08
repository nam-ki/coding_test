def solution(num, total):
    answer = []

    sum_value = sum(list(range(0,num)))

    a= (total - sum_value)//num

    answer.append(a)

    for i in range(1,num):
        answer.append(answer[i-1]+1)

    return answer

num = 3
total = 0
result = solution(num,total)

print(result)