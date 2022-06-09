list1 = ["Shogun","Tapioca Express","Burger King","KFC"] 
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
lt = set(list1) & set(list2)
mn = len(list1) + len(list2)
for i in lt:
  if list1.index(i)+list2.index(i) < mn:
    mn = list1.index(i)+list2.index(i) 
    rt = i
rt = [rt]
for i in lt:
  if list1.index(i)+list2.index(i) == mn:
    rt.append(i)
print(rt[1:])