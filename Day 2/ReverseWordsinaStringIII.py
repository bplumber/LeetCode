s = "Let's take LeetCode contest"
t = ""
for i in list(s.split(" ")):
  t= t + i[::-1] + " "
t=t[:-1]
print(t)