mat = [[1,2,3],[4,5,6]]
r = 3
c = 2
if r*c!=len(mat)*len(mat[0]):
  print(mat)
flattened = sum(mat, [])
x = 0
new_matrix = []
temp_matrix = []
for i in range(r):
  for j in range(c):
    temp_matrix.append(flattened[x])
    x+=1
  new_matrix.append(temp_matrix)
  temp_matrix = []
print(new_matrix)