#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
N-Queens Problem
http://www.csplib.org/Problems/prob054/
https://mathworld.wolfram.com/QueensProblem.html
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
            print(c("int", v("x",i,j), 0, 1))
    for i in range(0, n):
        xs = [v("x",i,j) for j in range(0, n)]
        exact_k(1, xs, opts)
    for j in range(0, n):
        xs = [v("x",i,j) for i in range(0, n)]
        exact_k(1, xs, opts)
    for u in range(0, 2*n-1):
        xs = [v("x",i,u-i) for i in range(0, n) if 0 <= u-i and u-i < n]
        atmost_k(1, xs, opts)
    for d in range(-n+1, n):
        xs = [v("x",i,i-d) for i in range(0, n) if 0 <= i-d and i-d < n]
        atmost_k(1, xs, opts)

"""
モデル1 (遅くなるようだ...)
各対角線に対しクイーンの有無を表す補助ブール変数を導入し，その和がnに等しい制約を追加する．
"""
def model1(n):
    for i in range(0, n):
        for j in range(0, n):
            print(c("int", v("x",i,j), 0, 1))
    for i in range(0, n):
        xs = [v("x",i,j) for j in range(0, n)]
        exact_k(1, xs, opts)
    for j in range(0, n):
        xs = [v("x",i,j) for i in range(0, n)]
        exact_k(1, xs, opts)
    for u in range(0, 2*n-1):
        print(c("int", v("u",u), 0, 1))
        xs = [v("x",i,u-i) for i in range(0, n) if 0 <= u-i and u-i < n]
        # v("u",u) == sum of xs
        exact_k(1, [c("-", 1, v("u",u))] + xs, opts)
    us = [v("u",u) for u in range(0, 2*n-1)]
    exact_k(n, us, opts)
    for d in range(-n+1, n):
        print(c("int", v("d",d), 0, 1))
        xs = [v("x",i,i-d) for i in range(0, n) if 0 <= i-d and i-d < n]
        # v("d",d) == sum of xs
        exact_k(1, [c("-", 1, v("d",d))] + xs, opts)
    ds = [v("d",d) for d in range(-n+1, n)]
    exact_k(n, ds, opts)

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
        ok = ok and sum(xs) == 1
    for j in range(0, n):
        xs = [sol[v("x",i,j)] for i in range(0, n)]
        ok = ok and sum(xs) == 1
    for u in range(0, 2*n-1):
        xs = [sol[v("x",i,u-i)] for i in range(0, n) if 0 <= u-i and u-i < n]
        ok = ok and sum(xs) <= 1
    for d in range(-n+1, n):
        xs = [sol[v("x",i,i-d)] for i in range(0, n) if 0 <= i-d and i-d < n]
        ok = ok and sum(xs) <= 1
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
    print(f"; N-Queens モデル{model} n={n} opts={opts}")
    if model == "0":
        model0(n)
    elif model == "1":
        model1(n)
    else:
        raise NotImplementedError(f"不明なモデル {model}")

if __name__ == "__main__":
    main()
