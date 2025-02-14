t, s, h = int(input()), int(input()), int(input())
for i in range(t):
    print("*" + " " * s + "*" + " " * s + "*")
print("*" * (3 + 2 * s))
for i in range(h):
    print(" " * (1 + s) + "*")