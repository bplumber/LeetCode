def merge_the_tools(string, k):
    x = 0
    rt = ""
    for i in string:
        x+=1
        if i not in rt:
            rt+=i
        if x == k:
            print(rt)
            x, rt = 0, ""