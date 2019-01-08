import sys

# https://leetcode.com/problems/string-to-integer-atoi/

def atoi(str):
    str = str.strip()
    if len(str) == 0:
        return 0

    isNegative = False
    isDigit = False
    if str[0] == '-':
        isNegative = True
    elif str[0] == '+':
        pass
    elif str[0].isdigit():
        isDigit = True
    else:
        return 0
    i = 0
    if isDigit == False:
        i = 1
    num = ''
    while i < len(str):
        if str[i].isdigit() == True:
            num += str[i]
        else:
            break
        i += 1
    if num == '':
        return 0
    if isNegative:
        num = 0 - int(num)
    else:
        num = int(num)
    if num > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif num < -(2 ** 31):
        return -(2 ** 31)
    return num


def main():
    str = input('input: ')
    num = atoi(str)
    print('output: ', num)


if __name__ == '__main__':
    main()