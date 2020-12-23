from sys import stdin

n = int(input())
m = int(input())
field = [list(map(str, input().split())) for _ in range(n)]

def dfs(x, y):
    field[x][y] = '.'
    dx = -1
    while dx <= 1:
        dy = -1
        while dy <= 1:
            nx = x + dx
            ny = y + dy

            if 0 <= nx and nx < n and 0 <= ny and ny < m and field[nx][ny] == 'w':
                dfs(nx, ny)

            dy += 1
        dx += 1
    return 

def main():
    res = 0
    i = 0
    while i < n:
        j = 0
        while j < m:
            if field[i][j] == 'w':
                dfs(i, j)
                res += 1
            j += 1
        i += 1
    
    print(res)

if __name__ == "__main__":
    main()
