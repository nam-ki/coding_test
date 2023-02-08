def solution(num, total):
    answer = []

    middle_value = total // num
    answer.append(middle_value)

    count = 1

    for i in range(num-1):
        if i%2 ==0:
            after = middle_value + count
            answer.append(after)
        elif i%2 !=0:
            before = middle_value - count
            answer.append(before)
            count += 1

    answer.sort()
    return answer



num = 3
total = 0
result = solution(num,total)

print(result)