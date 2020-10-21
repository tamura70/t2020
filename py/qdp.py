#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Queen Domination Problem
https://oeis.org/A075458
https://mathworld.wolfram.com/QueenGraph.html
https://mathworld.wolfram.com/DominationNumber.html
"""

import sys
import getopt
from util import *

# オプション
opts = dict()

"""
モデル0
"""
def model0(n, d):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(c("int", v("q",i,j), 0, 1))
    qs = [v("q",i,j) for i in range(1, n+1) for j in range(1, n+1)]
    atmost_k(d, qs, opts)
    for i in range(1, n+1):
        for j in range(1, n+1):
            q_row = [v("q",i,j1) for j1 in range(1, n+1)]
            q_col = [v("q",i1,j) for i1 in range(1, n+1)]
            q_up = [v("q",i1,-i1+i+j) for i1 in range(1, n+1) if 1 <= -i1+i+j and -i1+i+j <= n]
            q_down = [v("q",i1,i1-i+j) for i1 in range(1, n+1) if 1 <= i1-i+j and i1-i+j <= n]
            qs = q_row + q_col + q_up + q_down
            cs = [c(">", q, 0) for q in qs]
            print(c("or", " ".join(cs)))

"""
モデル1
"""
def model1(n, d):
    raise NotImplementedError("未実装")

"""
解の検証
"""
def verify(n, d):
    sol = read_solution()
    print("Verify Sugar output")
    print("solution =", sol)
    ok = True
    qs = [sol[v("q",i,j)] for i in range(1, n+1) for j in range(1, n+1)]
    ok = ok and sum(qs) <= d
    for i in range(1, n+1):
        for j in range(1, n+1):
            q_row = [v("q",i,j1) for j1 in range(1, n+1)]
            q_col = [v("q",i1,j) for i1 in range(1, n+1)]
            q_up = [v("q",i1,-i1+i+j) for i1 in range(1, n+1) if 1 <= -i1+i+j and -i1+i+j <= n]
            q_down = [v("q",i1,i1-i+j) for i1 in range(1, n+1) if 1 <= i1-i+j and i1-i+j <= n]
            qs = [sol[q] for q in q_row + q_col + q_up + q_down]
            ok = ok and sum(qs) >= 1
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
    if "-h" in opts or len(args) != 2:
        print("Usage: %s n d" % sys.argv[0])
        return
    n = int(args[0])
    d = int(args[1])
    if "-v" in opts:
        verify(n, d)
        return
    model = opts.get("-m", "0")
    print(f"; QDP モデル{model} n={n} d={d} opts={opts}")
    if model == "0":
        model0(n, d)
    elif model == "1":
        model1(n, d)
    else:
        raise NotImplementedError(f"不明なモデル {model}")

if __name__ == "__main__":
    main()
