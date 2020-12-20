# -*- coding: utf-8 -*-

def main():
    a = ['e', 'B', 'd', 'C', 'a']
    print(sorted(a))
    print(sorted(a, key=lambda x: x.upper()))

if __name__ == "__main__":
    main()
