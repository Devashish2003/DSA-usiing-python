def find_factors():
    num = int(input("Enter a number"))
    factors = []
    if num>1:
        factors = [1, num]
    elif num == 1:
        return(factors[1])
    elif num==0:
        return(factors[0])
    max_fac = int(num/2) + 1
    for i in range(2,max_fac):
        if num % i == 0:
            factors.append(i)
    return sorted(factors)


print(find_factors())



def find_factors_optimized_method():
    num = int(input("Enter a number"))
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            x = num // i
            if i == x:
                factors.append(i)
            else:
                factors.extend([i, x])
    return sorted(factors)

print(find_factors_optimized_method())