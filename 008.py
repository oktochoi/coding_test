words = input()
stack = []

for word in words:
    if len(stack) == 0:
        if word == ")":
            print("No")
            exit()

    if word == "(":
        stack.append(word)
    else:
        stack.pop()

        
if len(stack) > 0:
    print("No")
else:
    print("Yes")