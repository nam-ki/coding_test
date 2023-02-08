def solution(babbling):
    answer = 0
    can_answer_list = ['aya','ye','woo','ma']

    for text in babbling:
        for can_answer in can_answer_list:
            if text == ' ':
                break
            elif text != '' and can_answer in text:
                text = text.replace(can_answer,' ',1)
                #발음 가능한 단어를 replace를 이용하여 한번만 ' '로 치환하여 제거가능.
            print(text)
        if text.replace(' ','') == '':
            #여러개의 발음을 통해 치환된 ' '들을 ''로 치환한 뒤, babbling이 '' 즉, 비교가능한 문자가 없을 시, answer에 1 추가
            answer += 1
    print(answer)
    return answer

babbling = ["aya", "yee", "u", "maa", "wyeoo"]

solution(babbling)