def secondlargest(arr):
    mx=float('-inf')
    for i in arr:
        if i > mx:
            mx=i
    c=0
    for i in arr:
        if i==mx:
            c+=1
    if len(arr)!=c:
        return 1
    else:
        return -1
arr=list(map(int,input().split()))
print(secondlargest(arr))