# -*- coding: utf-8 -*-

def main():

    a = [1,2,3] + [4,5]
    print(a)
    b = [1,2,3] * 3
    print(b)
    # list に存在するか確認
    print(1 in a)
    print(99 in a)
    # イデックス指定の削除
    del a[1]
    print(a)
    # スライスで指定で削除
    del b[1:3]
    print(b)
    x = b.pop(1)
    print(x)
    c = [1,2,3,4,5]
    # オブジェクト指定で削除
    c.remove(3)
    print(c)

if __name__ == "__main__":
    main()
