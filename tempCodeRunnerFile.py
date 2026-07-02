num = input()
new_num = []
for x in range(len(num)):
    new_num.append(num[len(num)-x-1])
print(new_num)