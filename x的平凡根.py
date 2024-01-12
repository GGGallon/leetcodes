def fun(x):
    left = 0
    right = x-1
    index = -1
    while left <= right:
        mid = (left+right)//2
        if mid**2 <= x:
            if index < mid:
                index = mid
            left = mid + 1
        elif mid**2 > x:
            right = mid - 1
    return index



print(fun(4))