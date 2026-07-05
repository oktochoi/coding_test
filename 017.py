number = int(input())
res = int(input())
d = {}
count = 0

for _ in range(number):
    num = int(input())
    if res - num in d:
        print(d[res-num],count)
        exit()
    d[num] = count
    count += 1

print("None")