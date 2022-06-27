def positive_numbers(a):
    for i in a:
        if i<0:
            a.remove(i)
    return a


Input=list(map(int,input().split(",")))
print(positive_numbers(Input))