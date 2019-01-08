import sys

# https://leetcode.com/problems/divide-two-integers/

def divide(dividend, divisor):
    isNegative = 0
    if dividend < 0:
        isNegative += 1
    if divisor < 0:
        isNegative += 1
    if isNegative % 2 == 0:
        isNegative = False
    else:
        isNegative = True
    
    # if abs(divisor) == 1:
    #     if isNegative:
    #         return 0 - abs(dividend)
    #     else:
    #         return abs(dividend)

    dividend = abs(dividend)
    divisor = abs(divisor)    
    quotient = 0
    # sum = divisor
    # while sum <= dividend:
    #     sum += divisor
    #     quotient += 1
    #     if quotient > 2 ** 31 - 1:
    #         if isNegative:
    #             return -(2 ** 31)
    #         else:
    #             return 2 ** 31 - 1
    # if isNegative:
    #     quotient = 0 - quotient
    # return quotient
    
    count = 1
    denom = divisor
    while denom <= dividend:
        denom *= divisor
        count *= divisor
    print('count:', count)
    print('denom: ', denom)


def main():
    str = input('input: ')
    dividend, divisor = str.split()
    result = divideNew(int(dividend), int(divisor))
    print('output: ', result)


if __name__ == '__main__':
    main()