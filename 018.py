number = int(input())
d = {}

for _ in range(number):
    num = int(input())
    if num in d:
        print(d[num])
        exit()
    d[num] = num
print("None")