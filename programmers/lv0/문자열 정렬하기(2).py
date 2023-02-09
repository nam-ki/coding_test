def solution(my_string):
    my_string = my_string.lower()

    answer = sorted(my_string)

    answer = ''.join(answer)

    return answer

my_string = "Python"

result = solution(my_string)

print(result)
