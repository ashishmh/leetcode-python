import sys

# https://leetcode.com/problems/reverse-words-in-a-string/

def reverseWords(str):
    words = str.split()
    i = 0
    j = len(words) - 1
    while (i != j and i != j + 1):
        temp = words[i]
        words[i] = words[j]
        words[j] = temp
        i += 1
        j -= 1
    reverseStr = ' '.join(words)
    return reverseStr


def main():
	str = input('input: ')
	reverseStr = reverseWords(str)
	print('reverse string: ', reverseStr)


if __name__ == '__main__':
    main()