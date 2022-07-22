def runCustomerSimulation(n, s):
  res = 0 
  st = set()
  for i in s:
    if i not in st:
      if n!=0:
        st.add(i)
        n-=1
      else:
        res+=1
    else:
      st.remove(i)
      n+=1
  return res//2