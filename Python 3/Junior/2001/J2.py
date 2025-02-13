def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
x = int(input())
m = int(input())
gcd, inverse, _ = gcd_extended(x, m)
if gcd != 1:
    print("No such integer exists.")
else:
    print(inverse % m)