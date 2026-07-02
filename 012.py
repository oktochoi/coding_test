words = input()
stack = []

for ch in words:
    if len(stack) == 0:
        stack.append(ch)
    else:
        if ch == stack[len(stack)-1]:
            stack.pop()
        else:
            stack.append(ch)

if len(stack) == 0:
    print("Empty")
else:
    print("".join(stack))