#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
All-Interval Series (AIS)
http://www.csplib.org/Problems/prob007/
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
        print(c("int", v("x",i), 0, n-1))
    xs = [v("x",i) for i in range(0, n)]
    alldiff_sugar(xs)
    for i in range(1, n):
        print(c("int", v("d",i), 1, n-1))
        print(c("=", v("d",i), c("abs", c("-", v("x",i-1), v("x",i)))))
    ds = [v("d",i) for i in range(1, n)]
    alldiff_sugar(ds)
    # 自明な解の除去
    if "-t" in opts:
        print(c("!=", v("d",1), 1))
        print(c("!=", v("d",n-1), 1))

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
    xs = [sol[v("x",i)] for i in range(0, n)]
    ok = ok and verify_alldiff(xs)
    ds = [sol[v("d",i)] for i in range(1, n)]
    ok = ok and verify_alldiff(ds)
    if ok:
        print("Verify OK")
    else:
        print("Verify NG")

"""
メイン
"""
def main():
    global opts
    o, args = getopt.getopt(sys.argv[1:], "hvm:t", ["bc="])
    opts = dict(o)
    if "-h" in opts or len(args) != 1:
        print("Usage: %s n" % sys.argv[0])
        return
    n = int(args[0])
    if "-v" in opts:
        verify(n)
        return
    model = opts.get("-m", "0")
    print(f"; AIS モデル{model} n={n} opts={opts}")
    if model == "0":
        model0(n)
    elif model == "1":
        model1(n)
    else:
        raise NotImplementedError(f"不明なモデル {model}")

if __name__ == "__main__":
    main()
