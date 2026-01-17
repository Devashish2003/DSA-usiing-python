def merge(nums1, m, nums2, n):
    i = m - 1        # pointer for nums1 valid elements
    j = n - 1        # pointer for nums2
    k = m + n - 1    # pointer for nums1 buffer end

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    # Example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    merge(nums1, m, nums2, n)
    print(nums1)   # [1, 2, 2, 3, 5, 6]

    # Example 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0

    merge(nums1, m, nums2, n)
    print(nums1)   # [1]

    # Example 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    merge(nums1, m, nums2, n)
    print(nums1)   # [1]
