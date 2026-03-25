m = [1,5,3,2,2,1,5,5,7,5,10]
n = [10,111,1,9,5,67,2,5,4,8,5,88]

# calculate the frequency of elements of n in m

def hashing(m,n):
    hash_list = [0]*11
    for i in m:
        hash_list[i] += 1
    print("Element\tFrequency")
    for num in n:
        if num<1 or num>10:
            print(num,":\t 0")
        else:
            print(num,":\t ",hash_list[num])


hashing(m,n)
