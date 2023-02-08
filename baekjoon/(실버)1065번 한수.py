num = input()

def solve(num):
    count=0
    for i in range(1,int(num)+1):
        if i<100:
            count += 1
        else:
            if {(i//100)-(i//10%10)} == {(i//10%10)-(i%100%10)}:
                #세번째 자리수 - 두번째 자리수 == 두번째 자리수 == 첫번째 자리수
                count += 1
    return count

result = solve(num)
print(result)
