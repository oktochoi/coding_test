num = int(input())

num_list = []
total = 0
count = 0
for _ in range(num):
    new_number = int(input())
    total += new_number
    num_list.append(new_number)

average = total/num

for x in num_list:
    if x > average:
        count +=1

print(count)
