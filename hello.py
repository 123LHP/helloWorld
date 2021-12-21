#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   hello.py
@Time    :   2021/12/20 15:46:27
@Author  :   Designer 
@Version :   1.0
@Contact :   NULL
@WebSite :   NULL
'''
# Start typing your code from here


import os
import argparse
import matplotlib.pyplot as plt
import numpy as np

def get_args():
    parser = argparse.ArgumentParser(description='向某人打招呼')
    parser.add_argument('person', nargs='?', help='指定打招呼对象')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.person == None:
        args.person = 'world'
    print(f'hello, {args.person}!')

img=np.zeros((10,10))
plt.imshow(img,cmap="gray")
plt.show()