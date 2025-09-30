def binary_search(lst, tr, max, min):

    mid_point = (max + min) // 2
    
    if tr == lst[mid_point]:
        return mid_point
    
    elif tr < lst[mid_point]:   # if Target is less then midpoint the true
        return binary_search(lst, tr, mid_point - 1, min)
    else:
        return binary_search(lst, tr, max, mid_point + 1)

        
lst = [1,2,6,8,10,11]
tr = 10
result = binary_search(lst, tr, len(lst) - 1, 0)
print('The index: ', result)