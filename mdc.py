import random
from math import log2
i = 0
j = 0
k=0

def mdc(a,b):
    global i
    i+=1
    if a==b: return a
    if a%b == 0: return b
    
    return mdc(b,a%b)
    
def mdc_(a,b):
    global j
    j += 1
    
    if a == b: return a
    if a == 0: return b
    if b == 0: return a
    
    if a%2 == 0 and b%2 == 0:
        return 2*mdc_(a//2, b//2)
        
    elif b%2 == 0:
        return mdc_(a, b//2)
        
    elif a%2 == 0:
        return mdc_(a//2,b)
        
    elif a > b:
        return mdc_((a-b)//2,b)
    else:
        return mdc_((b-a)//2,a)
        
def mdc_stein(a, b):
    global k
    k+=1
    
    if a == b: return a
    if a == 0: return b
    if b == 0: return a

    if (a & 1) == 0 and (b & 1) == 0:
        return 2 * mdc_stein(a >> 1, b >> 1)

    elif (a & 1) == 0:
        return mdc_stein(a >> 1, b)

    elif (b & 1) == 0:
        return mdc_stein(a, b >> 1)

    elif a > b:
        return mdc_stein((a - b) >> 1, b)
    else:
        return mdc_stein((b - a) >> 1, a)
        
x = 21
y = 13
w = 1000000
z = 1

print(mdc(x, y), f"chamadas: {i}")
print(mdc_stein(x, y),f"chamadas: {k}")
print("pior caso: ", int(log2(min(x,y))+1))

i = 0
k = 0
print(mdc(w,z), f"chamadas {i}")
print(mdc_stein(w,z),f"chamadas {k}")
