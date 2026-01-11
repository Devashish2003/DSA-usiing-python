from math import *
def count_digit(num)->int:
    return int(log10(num)) + 1

result = count_digit(int(input('Enter a number: ')))
print(result)


"""logic
log10(5438)=3.735, and if we add 1 to 3.735 and convert to integer it would be 4 that means 4 digit number

log10(177715)=5.294,  and if we add 1 to 5.294 and convert to integer it would be 6 that means 6 digit number"""