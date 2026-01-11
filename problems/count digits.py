def count_digits(num)->int:
    count = 0
    while num>0:
       num //=10
       count += 1
    return count 
    
print(count_digits(int(input('Enter a number: '))))