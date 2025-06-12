import math

# encontrar mediana
def trivial(v):
    v = sorted(v)
    n = len(v)
    if n%2 == 1:
        return v[n//2]
    else:
        return (v[n//2] + v[n//2 -1])/2
        
print(trivial([5,4,1,3,4,2,1,8,2]))

def median(v):
    n = len(v)
    if n%2 == 1:
        return quickselect(v,0,n-1,n//2)
    else:
        return 0.5*(quickselect(v,0,n-1,n//2 -1) + quickselect(v,0,n-1,n//2))
        
def quickselect(v, l, r, k):
    p = partition(v,l,r)
    if p == k:
        return v[p]
    elif p < k:
        return quickselect(v,p+1,r,k)
    else:
        return quickselect(v,l,p-1,k)
    
    
g = 0
h = 0
w = 0
t = 0

def partition(v, l, r):
    global g
    g+=1
    pivo = v[r] # arbitrario
    i = l
    for j in range(l,r):
        if v[j] <= pivo: # se for menor vai pro começo
           v[j], v[i] = v[i], v[j]
           i+=1
    v[i], v[r] = v[r], v[i]
    return i

def quicksort(v, l, r):
    global h
    h+=1
    if l < r:
       p = partition(v, l, r)
       quicksort(v,l,p-1)
       quicksort(v,p+1,r)
    
def quicKsort(v, l, r, k):
    global w
    w+=1
    if l < r:
       if r - l + 1 > k:
          p = partition(v, l, r)
          quicKsort(v,l,p-1,k)
          quicKsort(v,p+1,r,k)
       else:
          bubblesort(v,l,r)
 
def bubblesort(v,l,r):
    global t
    t+=1
    for i in range(l,r):
       for j in range(l,r-i-1):
          if v[j] > v[j+1]:
               v[j],v[j+1] = v[j+1], v[j]
               
v = [1,2,3,7,10,5,27,34,42]
quicksort(v,0,len(v)-1)
print(v)
print(f"{g} particoes, {h} quicksorts")
g = 0
v = [1,2,3,7,10,5,27,34,42]
quicKsort(v,0,len(v)-1,2)
print(v)
print(f"{g} particoes, {w} quicKsorts, {t} bubblesorts")

print(median(v))

# QUAL O VALOR DE K IDEAL?

# O(nk + nlog(n/k)) < O(nlogn)

# k < c*logn - log(n/k)
# k < (c-1)log(n/k)

# 2^k < (c-1)n/k

# k*2^k < C*n

# OUTRA ABORDAGEM

# O(nk + nlog(n/k)) < O(nlogn)

# f(k) = nk + nlogn
# f(k) = nk + nlogn - nlogk
# (n e c são constantes)

# f(k) = k - log2(k)
# f(k) = k - ln(k) * 1/ln(2)

# df/dk = 1 - 1/k*ln(2)

# min -> df/dk = 0

# 1/kln(2) = 1
# k = 1/ln(2)

k = 1/math.log(2)
print(k) # 1.442




    
        
        
        
    

