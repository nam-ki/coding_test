import sys

#입출력 방식이 느리면 여러줄을 입력받거나 출력할 때 시간 초과 가능
#파이썬의 경우, input 대신 sys.stdin.readline 사용 가능

T = int(sys.stdin.readline()) #테스트 케이스의 갯수 입력

result_list = []

for i in range(T):
    A,B = map(int,sys.stdin.readline().split(' '))
    result = A+B
    result_list.append(result)

for i in range(T):
    print(result_list[i])