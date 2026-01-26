"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one."""
def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

