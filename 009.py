words = input()
stack = []

for word in words:
    if word != "x":
        stack.append(word)

print("".join(stack))