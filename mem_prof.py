#!/usr/bin/env python3
@profile
def my_func():
    a = (x for x in range(int(1e7)))
    b = [x for x in range(int(1e7))]
    del b
    return a

if __name__ == '__main__':
    my_func()
