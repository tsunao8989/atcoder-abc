# -*- coding: utf-8 -*-

def main():
    a = [2,5,1,4,3]
    b = sorted(a)
    print(a)
    print(b)

    a.sort()
    print(a)

    c = sorted(a, reverse=True)
    print(c)

if __name__ == "__main__":
    main()
