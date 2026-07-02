words = input()
count = 0
for word in words:
    if word in "aeiou":
        count +=1

print(count)