#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Costas Array Problem
http://www.csplib.org/Problems/prob076/
https://en.wikipedia.org/wiki/Costas_array
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
    for j in range(0, n):
        print(c("int", v("x",0,j), 1, n))
    xs = [v("x",0,j) for j in range(0, n)]
    alldiff_sugar(xs)
    for i in range(1, n):
        for j in range(0, n-i):
            print(c("int", v("x",i,j), -n+1, n-1))
            print(c("!=", v("x",i,j), 0))
            print(c("=", v("x",i,j), c("-", v("x",0,j), v("x",0,i+j))))
        xs = [v("x",i,j) for j in range(0, n-i)]
        alldiff_sugar(xs)

"""
モデル1
"""
def model1(n):
    raise NotImplementedError("未実装")

"""
解の検証
"""
def verify(n):
    sol = read_solution()
    print("Verify Sugar output")
    print("solution =", sol)
    ok = True
    for i in range(0, n):
        if i > 0:
            for j in range(0, n-i):
                ok = ok and sol[v("x",i,j)] == sol[v("x",0,j)] - sol[v("x",0,i+j)]
        xs = [sol[v("x",i,j)] for j in range(0, n-i)]
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
    o, args = getopt.getopt(sys.argv[1:], "hvm:", ["bc="])
    opts = dict(o)
    if "-h" in opts or len(args) != 1:
        print("Usage: %s n" % sys.argv[0])
        return
    n = int(args[0])
    if "-v" in opts:
        verify(n)
        return
    model = opts.get("-m", "0")
    print(f"; Costas Array モデル{model} n={n} opts={opts}")
    if model == "0":
        model0(n)
    elif model == "1":
        model1(n)
    else:
        raise NotImplementedError(f"不明なモデル {model}")

if __name__ == "__main__":
    main()
