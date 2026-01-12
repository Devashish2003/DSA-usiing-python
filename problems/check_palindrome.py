def check_palindrome(num):
    result = 0
    temp_num = num
    while num > 0:
        r = num % 10
        result =result *10 + r
        num = num // 10
    """if temp_num == result:
        return True
    else:
        return False"""
    return result == temp_num


print(check_palindrome(17))
print(check_palindrome(121))


# Time Complexity = O(log10(N))
# Space Complexity =  O(1)         as only two variables are used and they are constant