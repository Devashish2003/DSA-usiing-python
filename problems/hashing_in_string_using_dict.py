s = "sdkfjhweiruhskjfhksjbvakshjfaisduhfaksjdhf"
c = ['c','f','h','t','b','s','d','l','w']

def hashing_dict(str, ch):
    hash_map = dict()
    for st in str:
        if st in hash_map:
            hash_map[st] += 1
        else:
            hash_map[st] = 1
    print("Element\tFrequency")
    for c in ch:
        print(c, "\t", hash_map.get(c, 0))



hashing_dict(s,c)
