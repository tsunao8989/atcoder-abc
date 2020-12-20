# -*- coding: utf-8 -*-

def main():
    d = [[1,2,3],[4,5,6],[7,8,9]]
    print(d)
    td = [x for x in zip(*d)]
    print(td)
    print([sum(x) for x in zip(*d)])

if __name__ == "__main__":
    main()
