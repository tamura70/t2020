# -*- coding: utf-8 -*-

import sys
import re

counter = 0

def new_name():
    global counter
    counter = counter + 1
    return "_T" + str(counter)

def v(name, *args):
    indices = [str(x) for x in args]
    return name + "_" + "_".join(indices)

def t(name, *args):
    indices = [str(x) for x in args]
    return "_" + name + "_" + "_".join(indices)

def c(*args):
    elems = [str(x) for x in args]
    return "(" + " ".join(elems) + ")"

def atleast_1(xs):
    print("; atleast_1 " + " ".join(xs))
    ors = [c(">", x, 0) for x in xs]
    print(c("or", " ".join(ors)))

def atmost_1(xs):
    print("; atmost_1 " + " ".join(xs))
    for i in range(0, len(xs)):
        for j in range(i+1, len(xs)):
            print(c("<=", c("+", xs[i], xs[j]), 1))

def exact_1(xs):
    atleast_1(xs)
    atmost_1(xs)

def atleast_k_sugar(k, xs):
    print(c(">=", c("+", " ".join(xs)), k))

def atmost_k_sugar(k, xs):
    print(c("<=", c("+", " ".join(xs)), k))

def exact_k_sugar(k, xs):
    print(c("=", c("+", " ".join(xs)), k))

def atleast_k_sinz(k, xs):
    print("; atleast_k_sinz " + str(k) + " " + " ".join(xs))
    n = len(xs)
    s = new_name()
    print(c("int", v(s,0), 0))
    for i in range(0,n):
        print(c("int", v(s,i+1), 0, min(i+1, k)))
        print(c("<=", v(s,i+1), c("+", v(s,i), xs[i])))
    print(c(">=", v(s,n), k))
    return s

def atmost_k_sinz(k, xs):
    print("; atmost_k_sinz " + str(k) + " " + " ".join(xs))
    n = len(xs)
    s = new_name()
    print(c("int", v(s,0), 0))
    for i in range(0,n):
        print(c("int", v(s,i+1), 0, min(i+1, k)))
        print(c(">=", v(s,i+1), c("+", v(s,i), xs[i])))
    print(c("<=", v(s,n), k))
    return s

def exact_k_sinz(k, xs):
    print("; exact_k_sinz " + str(k) + " " + " ".join(xs))
    n = len(xs)
    s = new_name()
    print(c("int", v(s,0), 0))
    for i in range(0,n):
        print(c("int", v(s,i+1), 0, min(i+1, k)))
        print(c("=", v(s,i+1), c("+", v(s,i), xs[i])))
    print(c("=", v(s,n), k))
    return s

def atleast_k_sinz2(k, xs):
    n = len(xs)
    if k == 1:
        atleast_1(xs)
    elif k <= n-k:
        atleast_k_sinz(k, xs)
    else:
        atmost_k_sinz(n-k, [c("-", 1, x) for x in xs])

def atmost_k_sinz2(k, xs):
    n = len(xs)
    if k == n-1:
        atleast_1([c("-", 1, x) for x in xs])
    elif k <= n-k:
        atmost_k_sinz(k, xs)
    else:
        atleast_k_sinz(n-k, [c("-", 1, x) for x in xs])

def exact_k_sinz2(k, xs):
    n = len(xs)
    if k <= n-k:
        exact_k_sinz(k, xs)
    else:
        exact_k_sinz(n-k, [c("-", 1, x) for x in xs])

def atleast_k(k, xs, opts):
    bc = opts.get("--bc", "sugar")
    if bc == "sugar":
        atleast_k_sugar(k, xs)
    elif bc == "sinz":
        atleast_k_sinz(k, xs)
    elif bc == "sinz2":
        atleast_k_sinz2(k, xs)
    else:
        raise NotImplementedError("不明なブール基数制約の符号化 " + bc)

def atmost_k(k, xs, opts):
    bc = opts.get("--bc", "sugar")
    if bc == "sugar":
        atmost_k_sugar(k, xs)
    elif bc == "sinz":
        atmost_k_sinz(k, xs)
    elif bc == "sinz2":
        atmost_k_sinz2(k, xs)
    else:
        raise NotImplementedError("不明なブール基数制約の符号化 " + bc)

def exact_k(k, xs, opts):
    bc = opts.get("--bc", "sugar")
    if bc == "sugar":
        exact_k_sugar(k, xs)
    elif bc == "sinz":
        exact_k_sinz(k, xs)
    elif bc == "sinz2":
        exact_k_sinz2(k, xs)
    else:
        raise NotImplementedError("不明なブール基数制約の符号化 " + bc)

def channel_int(x, lb, ub):
    print("; channel_int " + x + " " + str(lb) + " " + str(ub))
    for a in range(lb, ub+1):
        print(c("int", t(x,a), 0, 1))
        print(c("iff", c(">", t(x,a), 0), c("=", x, a)))

def alldiff_sugar(xs):
    print(c("alldifferent", " ".join(xs)))

def alldiff_ohno(xs, lb, ub, opts):
    print("; alldiff_ohno " + " ".join(xs))
    n = len(xs)
    d = ub - lb + 1
    if n == 1:
        return
    if n == d:
        for a in range(lb, ub+1):
            ys = [t(xs[i],a) for i in range(0, n)]
            exact_k(1, ys, opts)
    else:
        z = new_name()
        for a in range(lb, ub+1):
            print(c("int", v(z,a), 0, 1))
        zs = [v(z,a) for a in range(lb, ub+1)]
        exact_k(d-n, zs, opts)
        for a in range(lb, ub+1):
            ys = [t(xs[i],a) for i in range(0, n)]
            exact_k(1, ys + [zs[a-lb]], opts)

def read_solution():
    sol = dict()
    for line in sys.stdin:
        m = re.match(r"^a\s+(\S+)\s+(-?\d+)$", line)
        if m == None:
            continue
        sol[m.group(1)] = int(m.group(2))
    return sol

def verify_alldiff(xs):
    n = len(xs)
    for i in range(0, n):
        for j in range(i+1, n):
            if xs[i] == xs[j]:
                return False
    return True
