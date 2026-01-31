def check_duplicate(nums: list[int]) -> bool:
    if len(nums) == 1:
        return False
    seen = {}
    for item in nums:
        if item in seen:
            return True
        seen[item] = 1
    return False

