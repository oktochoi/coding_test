words = input()
stack = []
for ch in words:
    if ch == "#":
        if len(stack) == 0:
            continue
        else:
            stack.pop()
    else:
        stack.append(ch)

print("".join(stack))