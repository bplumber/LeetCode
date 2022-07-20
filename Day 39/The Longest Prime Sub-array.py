def main():
  prime_nos = []
  def simpleSieve(limit):
      nonlocal prime_nos
      n = [True for i in range(limit+1)]
      for i in range(2,limit+1):
          if (n[i] == True):
              for j in range(2*i, limit+1, i):
                  n[j] = False
  
      for p in range(2, limit+1):
          if (n[p] == True):
              prime_nos.append(p)
  arr = [1, 2, 4, 3, 29, 11, 7, 8, 9]
  simpleSieve(max(arr))
  mx = 0 
  ct = 0
  for i in arr:
    if i in prime_nos:
      ct+=1
    else:
      if mx < ct:
        mx = ct
      ct = 0 
  print(mx)
main()