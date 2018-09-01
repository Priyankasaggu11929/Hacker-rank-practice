#!usr/bin/env python3

N=int(input())

def fib(n):
    n1,n2 = 0,1
    f=[]
    if n==1:
        f.append(n2)
        return f
    if n>=2:
        f.append(n2)
        for i in range(2,n):
            next=n1+n2
            f.append(next)
            n1=n2
            n2=next
        return f


def prime(N):
    primes  = []
    chkthis = 2
    while len(primes) < N:
        ptest    = [chkthis for i in primes if chkthis%i == 0]
        primes  += [] if ptest else [chkthis]
        chkthis += 1
    return primes

p1=prime(N)
f1=fib(N+1)

if N%2==0:
    N=int(N/2)-1
    print(p1[N])
else:
    N=int(N/2)
    print(f1[N])                                                                                                                       1,18          Top
