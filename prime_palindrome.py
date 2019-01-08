import sys
import math

# https://leetcode.com/problems/prime-palindrome/

def primePalindrome(n):
    if n == 1 or n == 2:
        return 2
    nextOdd = n
    if nextOdd % 2 == 0:
        nextOdd += 1
    for i in range(nextOdd, 2 * (10 ** 8), 2):
        if isPrime(i):
            if isPalindrome(i):
                return i
    return -1


def isPrime(n):
    if n == 0 or n == 1:
        return False
    if n > 2 and n % 2 == 0:
        return False
    factors = 0
    # for i in range(2, int(n/2)):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def isPalindrome(n):
    str1 = str(n)
    str2 = ''
    for i in range(len(str1)-1, -1, -1):
        str2 += str1[i]
    # print('str1: ', str1)
    # print('str2: ', str2)
    return str1 == str2


def main():
    str = input('input: ')
    output = primePalindrome(int(str))
    print('output: ', output)

    # print('prime check (10): ', isPrime(10))
    # print('prime check (25): ', isPrime(25))
    # print('prime check (29): ', isPrime(29))
    # print('prime check (5): ', isPrime(5))
    # print('prime check (1): ', isPrime(1))
    # print('prime check (0): ', isPrime(0))
    # print('prime check (2): ', isPrime(2))
    # print('prime check (99): ', isPrime(99))
    # print('prime check (101): ', isPrime(101))
    # print('prime check (6): ', isPrime(6))

    # print('palindrome check (101): ', isPalindrome(101))
    # print('palindrome check (1000): ', isPalindrome(1000))
    # print('palindrome check (12321): ', isPalindrome(12321))
    # print('palindrome check (1): ', isPalindrome(1))
    # print('palindrome check (11): ', isPalindrome(11))
    # print('palindrome check (12): ', isPalindrome(12))


if __name__ == '__main__':
    main()