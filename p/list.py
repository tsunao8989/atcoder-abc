# -*- coding: utf-8 -*-

def main():
    data = range(1, 1000)
    c = len([x for x in data if x % 3 == 0])
    print(c)
if __name__ == "__main__":
    main()
