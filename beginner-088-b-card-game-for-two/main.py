n = int(input())
a = list(map(int, input().split()))

sa = sorted(a, reverse=True)
print(sum(sa[0::2]) - sum(sa[1::2]))
