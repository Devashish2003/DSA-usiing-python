from math import pow
def check_armstrong(num)->bool:
    temp_num = num
    result = 0
    nod = len(str(temp_num))
    while num>0:
        r = num%10
        result += pow(r,nod)
        num = num//10
    return result == temp_num

print(check_armstrong(10))
print(check_armstrong(153))
print(check_armstrong(1634))

# time complexity = O(log10(N)
# space complexity = O(1)