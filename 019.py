words = input()
d ={}
count = 0

for word in words:
    if word in d:
        print(d[word],count)
        exit()
    d[word] = count
    count +=1
print("None")
