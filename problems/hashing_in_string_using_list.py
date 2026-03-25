s = "sdkjhqruhasdfbasgkjahsdsuduquhkajbvxnbckahsdfweiuhisauhdfkajsdhabv"
c = ['a','s','g','t','p','u','d','h']

def hashing_list(s,c):
    hash_list = [0]*26
    for ch in s:
        ascii = ord(ch)
        index = ascii - 97
        hash_list[index] += 1
    print("Element\tFrequency")
    for ch in c:
        ascii = ord(ch)
        index = ascii - 97
        print(ch,"\t",hash_list[index])


hashing_list(s,c)
