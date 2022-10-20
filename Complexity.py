import sys
import time

sys.setrecursionlimit(100000)

def computeSum1ToN(n):
    """
    Compute sum 1 + 2 + ... + n
    Time complexity = Number of operations performed = 3n
    For each i = 1, 2, ..., n, we have to perform 3 operations: i <= n, r + i and i + 1
    So in total, we do 3n operations.
    If we count assignments => 5n + 2.
    """
    r = 0
    i = 1
    while i <= n:
        r = r + i
        i = i + 1
    return r

def computeSum1ToNQuick(n):
    """
    Compute sum of 1 + 2 + ... + n using closed form formula
    Time complexity = 3
    """
    return n * (n + 1) // 2

def computeSum1ToNRecursion(n):
    if n == 0:
        return 0
    else:
        return computeSum1ToNRecursion(n - 1) + n

def compareRealTime():
    # real time vs. theoretical time complexity
    n = 10
    while n < 1000000000:
        start = time.time()
        R = computeSum1ToN(n)
        end = time.time()

        startQ = time.time()
        RQ = computeSum1ToNQuick(n)
        endQ = time.time()

        print("%20i     %.5f      %5f     %20i      %20i" % (n, end - start, endQ - startQ, R, RQ))
        n = 10 * n

compareRealTime()
