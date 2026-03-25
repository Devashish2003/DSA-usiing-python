def reverse(arr, left, right):
    while(left<right):
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1



arr = [1,2,3,4,5]
reverse(arr,0,len(arr)-1)
print(arr)
