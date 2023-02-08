import sys
N,M = map(int,sys.stdin.readline().split(' '))

number_list = list(map(int,sys.stdin.readline().split(' ')))

prefix_sum = [0]
#arr[0~a-1까지의 누적합]을 빼줘야 하므로 start=1을 대비해 0번째 인덱스로 0을 설정해야함.

result = 0
for i in number_list:
    #누적합 구하기
    result += i
    prefix_sum.append(result)

print(prefix_sum)

for i in range(M):
    first,end = map(int,sys.stdin.readline().split(' '))
    print(prefix_sum[end] - prefix_sum[first-1])
    #누적합은 arr[0~b까지의 누적합] - arr[0~a-1까지의 누적합)
