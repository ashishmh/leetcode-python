import sys

# leetcode link

def IsPrefix(x,y):
	if len(y) > len(x):
		return False
	for i in range(len(y)):
		if x[i] != y[i]:
			return False
	return True

# 1. Argument, return value
# 2. How to solve this problem by using the subproblem (use the return value of the subproblem)
# 3. Base case
def Solve(str, words):
	if len(str) == 0 and len(words) == 0:
		return True

	for i, w in enumerate(words):
		if IsPrefix(str, w):
			result = Solve(str[len(w):], words[0: i] + words[i + 1:])
			if result:
				return result	
	return False
			
def swap(input, i, j):
	return input[0 : i] + input[j] + input[i + 1: j] + input[i] + input[j+1:]

def permute (input, index):
	if index == len(input):
		return [input]
	result = []
	for i in range(index + 1, len(input)):
		result += permute (swap(input, index,i), index+1)

	return result


def main():
	# output = find_nearest_repetition(str)
	print (permute('ab', 0))

if __name__ == '__main__':
    main()