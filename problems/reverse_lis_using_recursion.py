def rev(arr, left, right):
    if left>=right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return rev(arr, left+1, right-1)


l = [1,2,3,4,5]
print(rev(l,0,4))

