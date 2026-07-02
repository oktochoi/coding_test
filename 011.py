words = input()
stack = []
count = ""

for ch in words:
    if ch != count:
        stack.append(ch)
        count = ch

print("".join(stack))