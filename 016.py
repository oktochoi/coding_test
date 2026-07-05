"""number = int(input())
res = int(input())
arr = []

for _ in range(number):
    num = int(input())
    arr.append(num)

count = 0

for x in range(number):
    count +=1
    for y in range(count,number):
        if arr[x] + arr[y] == res :
            print("Yes")
            exit()

print("No")"""

number = int(input())
res = int(input())
d = {}

for _ in range(number):
    num = int(input())
    if res-num in d:
        print("Yes")
        exit()
    d[num] = num
print("No")