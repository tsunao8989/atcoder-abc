# -*- coding: utf-8 -*-
from sys import stdin

def main():
    n = int(stdin.readline().rstrip())
    d = [stdin.readline().rstrip().split() for _ in range(n)]
    print(d)
    print(*d, sep='\n')

if __name__ == "__main__":
    main()
