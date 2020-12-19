# -*- coding: utf-8 -*-

def main():
    d = [[1,2,3],[4,5,6],[7,8,9]]
    print(d)
    f = [f for i in d for f in i]
    print(f)

if __name__ == "__main__":
    main()
