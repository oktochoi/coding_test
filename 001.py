num = int(input()) 
first_num = int(input())
max_num = first_num
min_num = first_num
for x in range(num-1): 
    new_num = int(input()) 
    if new_num > max_num: 
        max_num = new_num 
    if new_num < min_num: 
        min_num = new_num 
print(min_num, max_num)