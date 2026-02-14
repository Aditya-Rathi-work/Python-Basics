import math

def f(x):
    return x**3 - 4*x -9

def bisection(a, b , tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0 :
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None
    
    print("Iter \t a\t\t b\t\t c\t\t f(c)")
    for i in range(1, max_iter +1):
        c = (a + b) / 2
        print(f"{i}\t {a: .6f}\t {b: .6f}\t {c: .6f}\t {f(c): .6f}")

        if abs(f(c)) <tol:
            return c
        
        if f(a) * f(c) < 0:
            b=c
        else:
            a=c
            return (a + b) / 2
a = 2
b = 3   

root = bisection(a,b)

if root is not None:
    print(f"\nRoot = {root: .6f}")