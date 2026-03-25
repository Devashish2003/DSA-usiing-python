nums = [int(x) for x in input("Enter values: ").split()]
freq = dict()
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
