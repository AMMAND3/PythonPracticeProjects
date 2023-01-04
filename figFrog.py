# The Fibonacci sequence is defined using the following recursive formula:

#     F(0) = 0
#     F(1) = 1
#     F(M) = F(M - 1) + F(M - 2) if M >= 2
# A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and 
# wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. 
# Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

# The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions 
# from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

# 0 represents a position without a leaf;
# 1 represents a position containing a leaf.
# The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). 
# The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.


import math
Memo = {}

def fib(n: int):
    if n in Memo:
        return Memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    Memo[n] = fib(n - 1) + fib(n - 2)
    return Memo[n]

def solution(A):
    
    N = len(A)
    
    fibs = []
    i = 0
    while len(fibs)==0 or fibs[-1] < N+1:
        fibs.append( fib(i) )
        i += 1
    
    B = [-1] * (N+1)
    
    for i in range(0,N+1):
        leaf = lambda k: k>=N or A[k]==1
        
        if not leaf(i):
            B[i] = 0
        else:
            if i+1 in fibs:
                B[i] = 1
            else:
                candidates = []
                for f in fibs[1:]:
                    if i-f >= 0 and B[i-f] > 0:
                        candidates.append(B[i-f] + 1)
                
                B[i] = min(candidates) if len(candidates)>0 else 0
    
    return B[N] if B[N] > 0 else -1
