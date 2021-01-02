from math import log10

n, a, b = map(int, input().split())
s = 0

def digi(x):
    m, t  = int(log10(x)), 0
    for i in range(m, -1, -1):
        f = 10**i
        k = x // f
        t += k
        x -= k * f
    return t

for i in range(1, n + 1):
    if a <= digi(i) <= b:
       s += i
print(s)
