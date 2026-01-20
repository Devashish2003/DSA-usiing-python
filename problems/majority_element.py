def majority_element(nums):
    count = 0
    majority = None

    for num in nums:
        if count == 0:
            majority = num

        if num == majority:
            count += 1
        else:
            count -= 1

    return majority


print(majority_element([3, 3, 4, 3, 3]))
print(majority_element([3, 3, 4, 3, 3, 4, 4, 4, 4, 4]))