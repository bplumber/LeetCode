#Function to push an integer into the stack1.
def push1(a,x):
    i = 0
    while a[i]!=-1:
        i+=1
    a[i]= x
    
#Function to push an integer into the stack2.
def push2(a,x):
    a.append(x)
    
#Function to remove an element from top of the stack1.    
def pop1(a):
    i = 0
    while a[i]!=-1:
        i+=1
    if i > 0:
        x = a[i-1]
        a[i-1]=-1
        return x
    return -1
    
#Function to remove an element from top of the stack2.    
def pop2(a):
    if a[-1]!=-1:
        return a.pop()
    return -1