#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Queen Graph Coloring Problem
https://mathworld.wolfram.com/QueenGraph.html
https://mathworld.wolfram.com/VertexColoring.html
"""

import sys
import getopt
from util import *

# オプション
opts = dict()

"""
モデル0
"""
def model0(n):
    for i in range(0, n):
        for j in range(0, n):
            print(c("int", v("x",i,j), 0, n-1))
    for i in range(0, n):
        xs = [v("x",i,j) for j in range(0, n)]
        alldiff_sugar(xs)
    for j in range(0, n):
        xs = [v("x",i,j) for i in range(0, n)]
        alldiff_sugar(xs)
    for u in range(0, 2*n-1):
        xs = [v("x",i,u-i) for i in range(0, n) if 0 <= u-i and u-i < n]
        alldiff_sugar(xs)
    for d in range(-n+1, n):
        xs = [v("x",i,i-d) for i in range(0, n) if 0 <= i-d and i-d < n]
        alldiff_sugar(xs)
    if "-x" in opts:
        # 対称性除去
        for j in range(0, n):
            print(c("=", v("x",0,j), j))

"""
モデル1
大野さんの alldifferent を使用する．そのため，各整数変数について順序符号化と直接符号化をチャネリングする．
"""
def model1(n):
    for i in range(0, n):
        for j in range(0, n):
            print(c("int", v("x",i,j), 0, n-1))
            channel_int(v("x",i,j), 0, n-1)
    for i in range(0, n):
        xs = [v("x",i,j) for j in range(0, n)]
        alldiff_ohno(xs, 0, n-1, opts)
    for j in range(0, n):
        xs = [v("x",i,j) for i in range(0, n)]
        alldiff_ohno(xs, 0, n-1, opts)
    for u in range(0, 2*n-1):
        xs = [v("x",i,u-i) for i in range(0, n) if 0 <= u-i and u-i < n]
        alldiff_ohno(xs, 0, n-1, opts)
    for d in range(-n+1, n):
        xs = [v("x",i,i-d) for i in range(0, n) if 0 <= i-d and i-d < n]
        alldiff_ohno(xs, 0, n-1, opts)
    if "-x" in opts:
        # 対称性除去
        for j in range(0, n):
            print(c("=", v("x",0,j), j))

"""
解の検証
"""
def verify(n):
    sol = read_solution()
    print("Verify Sugar output")
    print("solution =", sol)
    ok = True
    for i in range(0, n):
        xs = [sol[v("x",i,j)] for j in range(0, n)]
        ok = ok and verify_alldiff(xs)
    for j in range(0, n):
        xs = [sol[v("x",i,j)] for i in range(0, n)]
        ok = ok and verify_alldiff(xs)
    for u in range(0, 2*n-1):
        xs = [sol[v("x",i,u-i)] for i in range(0, n) if 0 <= u-i and u-i < n]
        ok = ok and verify_alldiff(xs)
    for d in range(-n+1, n):
        xs = [sol[v("x",i,i-d)] for i in range(0, n) if 0 <= i-d and i-d < n]
        ok = ok and verify_alldiff(xs)
    if ok:
        print("Verify OK")
    else:
        print("Verify NG")

"""
メイン
"""
def main():
    global opts
    o, args = getopt.getopt(sys.argv[1:], "hvm:x", ["bc="])
    opts = dict(o)
    if "-h" in opts or len(args) != 1:
        print("Usage: %s n" % sys.argv[0])
        return
    n = int(args[0])
    if "-v" in opts:
        verify(n)
        return
    model = opts.get("-m", "0")
    print(f"; QGCP モデル{model} n={n} opts={opts}")
    if model == "0":
        model0(n)
    elif model == "1":
        model1(n)
    else:
        raise NotImplementedError(f"不明なモデル {model}")

if __name__ == "__main__":
    main()
