# -*- coding: utf-8 -*-

from copy import deepcopy

def main():
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = a[:]
    b[0].append(0)
    print(a)
    print(b)

    c = deepcopy(a)
    c[0].append(0)
    print(a)
    print(c)

if __name__ == "__main__":
    main()
