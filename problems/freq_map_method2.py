nums = [int(x) for x in input("Enter the value: ").split()]
freq = dict()

for i in range(0, len(nums)):
    freq[nums[i]] = freq.get(nums[i], 0) + 1

print(freq)
