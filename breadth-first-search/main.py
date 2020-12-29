#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

INF = 10000000
n, m  = 10, 10

maze = [
['#','S','#','#','#','#','#','#','.','#'],
['.','.','.','.','.','.','#','.','.','#'],
['.','#','.','#','#','.','#','#','.','#'],
['.','#','.','.','.','.','.','.','.','.'],
['#','#','.','#','#','.','#','#','#','#'],
['.','.','.','.','#','.','.','.','.','#'],
['.','#','#','#','#','#','#','#','.','#'],
['.','.','.','.','#','.','.','.','.','.'],
['.','#','#','#','#','.','#','#','#','.'],
['.','.','.','.','#','.','.','.','G','#']
]

sx, sy = 0, 1
gx, gy = 9, 8
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

class pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def bfs():
    que = deque([])
    d = [[INF for i in range(n)] for j in range(m)]
    que.append(pair(sx, sy))
    d[sx][sy] = 0
    #print(d)

    while len(que) != 0:
        p = que.popleft()
        if p.x == gx and p.y == gy:
            break
        for i in range(4):
            nx = p.x + dx[i]
            ny = p.y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < m and maze[nx][ny] != '#' and d[nx][ny] == INF:
                que.append(pair(nx, ny))
                d[nx][ny] = d[p.x][p.y] + 1

    return d[gx][gy]
        
print(bfs())

