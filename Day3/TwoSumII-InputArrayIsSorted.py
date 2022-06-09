numbers = [-3,3,4,90]
target = 0
if target == 0 and 0 in numbers:
    i1 = numbers.index(0)
    i2 = i1+1
    print([i1+1,i2+1])
number_set = set(numbers)
for i in number_set:
        if target/2 == i:
            i1 = numbers.index(i)
            i2 = numbers.index(i)+1
            break
        elif (target - i) in numbers:
            i1 = numbers.index(i)
            i2 = numbers.index(target - i)
            break
lt = [i1+1,i2+1]
lt.sort()
print(lt)