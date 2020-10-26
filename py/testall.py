#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import getopt
import os
import subprocess

csp = "/tmp/testall.csp"
log = "/tmp/testall.log"

"""
ais.py
"""
def test_ais():
    cmd = "./ais.py"
    n = 8
    for opts in ["-m0", "-m0 -t"]:
        cmd1 = f"{cmd} {opts} {n}"
        cmd2 = f"{cmd} -v {n}"
        verify(cmd1, cmd2)

"""
qdp.py
"""
def test_qdp():
    cmd = "./qdp.py"
    n = 8
    d = 5
    for opts in ["-m0 --bc=sugar", "-m0 --bc=sinz", "-m0 --bc=sinz2"]:
        cmd1 = f"{cmd} {opts} {n} {d}"
        cmd2 = f"{cmd} -v {n} {d}"
        verify(cmd1, cmd2)

"""
nqueens.py
"""
def test_nqueens():
    cmd = "./nqueens.py"
    n = 8
    for m in ["-m0", "-m1"]:
        for opts in ["--bc=sugar", "--bc=sinz", "--bc=sinz2"]:
            cmd1 = f"{cmd} {m} {opts} {n}"
            cmd2 = f"{cmd} -v {n}"
            verify(cmd1, cmd2)

"""
qgcp.py
"""
def test_qgcp():
    cmd = "./qgcp.py"
    n = 5
    for x in ["", "-x"]:
        for opts in ["-m0", "-m1 --bc=sugar", "-m1 --bc=sinz", "-m1 --bc=sinz2"]:
            cmd1 = f"{cmd} {x} {opts} {n}"
            cmd2 = f"{cmd} -v {n}"
            verify(cmd1, cmd2)

"""
costasarray.py
"""
def test_costasarray():
    cmd = "./costasarray.py"
    n = 5
    for opts in ["-m0"]:
        cmd1 = f"{cmd} {opts} {n}"
        cmd2 = f"{cmd} -v {n}"
        verify(cmd1, cmd2)

"""
検証の実行
"""
def verify(cmd1, cmd2):
    global csp
    global log
    print("################")
    if os.path.exists(csp):
        os.remove(csp)
    if os.path.exists(log):
        os.remove(log)
    run(f"{cmd1} >{csp}")
    run(f"sugar {csp} >{log}")
    run(f"{cmd2} <{log}")

def run(cmd):
    print(f"# Running: {cmd}")
    proc = subprocess.run(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    print(proc.stdout.decode("utf8"))
    
"""
メイン
"""
def main():
    test_ais()
    test_qdp()
    test_nqueens()
    test_qgcp()
    test_costasarray()

if __name__ == "__main__":
    main()
