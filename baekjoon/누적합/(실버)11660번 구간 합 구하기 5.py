import sys

N,M = map(int,sys.stdin.readline().split(' '))
test = []

#List comprehension 사용
# test = [0 for i in range(N)]
for i in range(N):
    test_in = list(map(int,sys.stdin.readline().split(' ')))
    test.append(test_in)

prefix_sum = []
prefix_sum_in = []
for i in range(N+1):
    prefix_sum_in.append(0)
prefix_sum.append(prefix_sum_in)

#1. 행과 열의 합으로 계산하는 방법
#행합
for i in range(N):
    result = 0
    prefix_sum_in = [0]
    for j in range(N):
        result += test[i][j]
        prefix_sum_in.append(result)
    prefix_sum.append(prefix_sum_in)


#열합
for i in range(N+1):
    result = 0
    for j in range(N+1):
        result += prefix_sum[j][i]
        prefix_sum[j][i]=result

# print(prefix_sum)

#2. prefix_sum을 이용하여 계산하는 방법
# #2차원 누적합 간단식
# sum_arr = [[0 for _ in range(N+1)]for _ in range(N+1)]
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         sum_arr[i][j] = test[i-1][j-1] + (sum_arr[i-1][j])+sum_arr[i][j-1] - sum_arr[i-1][j-1]
#         sum(prefix_sum)의 경우, N+1 X N+1로 구성되어 있어 상관없지만 test의 경우, NXN으로 구성되어 0부터 시작하는 인덱스에 맞추고자 i-1,j-1로 설정.
#         #본래 식은 sum_arr[i][j] = test[i][j] + (sum_arr[i-1][j])+sum_arr[i][j-1] - sum_arr[i-1][j-1] 이다.
# print(sum_arr)

for i in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split(' '))
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1]+prefix_sum[x1-1][y1-1])



