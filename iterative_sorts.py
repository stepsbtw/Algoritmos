# RECURSIVE ALGORITHMS

def merge_recursive(vL, vR, compare): # auxiliary O(n) space
  out = []
  i = j = 0
  # inserting
  while i < len(vL) and j < len(vR):
    if compare(vL[i], vR[j]): # rev
      out.append(vL[i])
      i += 1
    else:
      out.append(vR[j])
      j += 1
  # extending
  while i < len(vL):
    out.append(vL[i])
    i += 1
  while j < len(vR):
    out.append(vR[j])
    j += 1

  return out

def topdown_mergesort(v, l=0, r=None, compare=lambda x,y : x<y):
  if r == None:
    r = len(v)-1
  # base case
  if l == r:
    return [v[l]]
  # divide T(n//2)
  m = (l+r)//2
  vL = topdown_mergesort(v, l, m, compare)
  vR = topdown_mergesort(v, m+1, r, compare)
  # conquer O(n)
  return merge(vL, vR, compare)

def partition(v, l, r, compare):
  pivo = v[r] # random
  i = l
  for j in range(l,r):
    if compare(v[j], pivo):
      v[i], v[j] = v[j], v[i]
      i+=1
  v[i], v[r] = v[r], v[i]
  return i

def quicksort(v, l=0, r=None, compare=lambda x,y : x<y):  # inplace
  if r == None:
    r = len(v)-1
  if l < r:
    # divide (random)
    pidx = partition(v, l, r, compare)
    # conquer
    quicksort(v, l, pidx-1, compare)
    quicksort(v, pidx+1, r, compare)

def merge_iter(v, l1, r1, l2, r2, compare):
  out = []
  i, j = l1, l2

  while i <= r1 and j <= r2:
    if compare(v[i], v[j]):
      out.append(v[i])
      i += 1
    else:
      out.append(v[j])
      j += 1

  while i <= r1:
    out.append(v[i])
    i += 1
  while j <= r2:
    out.append(v[j])
    j += 1

  for k in range(len(out)):
        v[l1 + k] = out[k]

def topdown_mergesort_iter(v, l=0, r=None, compare=lambda x,y : x<y):
  if r == None:
    r = len(v)-1
  n = len(v)
  if n <= 1:
    return v
  stack = [(0, n-1, False)]
  while stack:
    l, r, divided = stack.pop()
    if l < r:
      m = (l + r) // 2
      if not divided:
        # dividir
        stack.append((l, r, True)) # marcar como dividido
        stack.append((m+1, r, 0)) # direita
        stack.append((l, m, 0)) # esquerda
      else:
        # intercalar [l:m] e [m+1:r]
        merge_iter(v, l, m, m+1, r, compare)

def bottomup_mergesort(v, compare=lambda x,y : x<y):
  n = len(v)
  tam = 1 # tamanho das sublistas

  while tam < n:
    for i in range(0, n, 2*tam):
      l1 = i
      r1 = min(i + tam-1, n-1)
      l2 = r1+1
      r2 = min(i + 2*tam-1, n-1)

      if l2 <= r2:
        merge_iter(v, l1, r1, l2, r2, compare)
    tam *= 2

  return v
