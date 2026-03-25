m = [1,5,3,2,2,1,5,5,8,7,5,10,15,4,5,78,6,5,3,2,65,46,4,8,98,100]
n = [4,5,8,7,9,6,55,5,8,46,98,7,8,6,20,100,200,54,6,3,5,4]

def hashing_dict(m,n):
    freq_map = dict()
    for num in m:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    print("Element\tFrequency")
    for num in n:
        if num in freq_map:
            print(num,":\t",freq_map[num])
        else:
            print(num,":\t 0")


hashing_dict(m,n)
