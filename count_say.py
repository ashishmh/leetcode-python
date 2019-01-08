import sys

# https://leetcode.com/problems/count-and-say/

def countAndSay(n):
    previousCode = ''
    currentCode = '1'
    for i in range(2, n+1):
        previousCode = currentCode
        currentCode = ''
        count = 1
        for j in range(len(previousCode) - 1):
            if previousCode[j+1] == previousCode[j]:
                count += 1
            else:
                currentCode += str(count) + str(previousCode[j])
                count = 1
        currentCode += str(count) + previousCode[(len(previousCode) - 1)]
    return currentCode


def main():
    str = input('input: ')
    output = countAndSay(int(str))
    print('output: ', output)


if __name__ == '__main__':
    main()