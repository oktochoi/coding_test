num = int(input())
new_dict= [0] * 101

for _ in range(num):
    new_num = int(input())
    new_dict[new_num]+=1

print(new_dict)

max_num = 0
idx=0
max_idx=0
for x in new_dict:
    if x > max_num:
        max_num = x
        max_idx = idx
    idx +=1

print(max_idx)