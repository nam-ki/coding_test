def solution(quiz):
    answer = []

    for text in quiz:
        ans = 0
        text_list = text.split(' ')

        if text_list[1] == '+':
            ans = int(text_list[0]) + int(text_list[2])
        elif text_list[1] == '-':
            ans = int(text_list[0]) - int(text_list[2])

        origin_ans = text_list[4]

        if str(ans) == origin_ans:
            answer.append('O')
        else:
            answer.append('X')

    return answer

quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

result = solution(quiz)

print(result)