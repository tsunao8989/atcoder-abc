n = int(input())
l = list(map(int, input().split()))
 
def solve(l, c=0):
    ll = [i / 2 for i in l if i % 2 == 0]
    if len(ll) != len(l):
        return c
    else:
        return solve(ll, c + 1)
 
print(solve(l))
