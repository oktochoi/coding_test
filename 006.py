words = input()
verify = 1
for x in range(len(words)//2):
    if words[x] == words[len(words)-x-1]:
        continue
    else:
        verify = 0

if verify == 1:
    print("Yes")
else:
    print("No")
