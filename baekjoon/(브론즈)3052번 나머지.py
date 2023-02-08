repeat_num = 10
save_late_num = []
for i in range(repeat_num):
    num = int(input())
    cal = num%42
    if cal not in save_late_num:
        save_late_num.append(cal)

print(len(save_late_num))
