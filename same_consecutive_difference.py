import sys

# https://leetcode.com/contest/weekly-contest-117/problems/numbers-with-same-consecutive-differences/

def numsSameConsecDiff(N, K):
	numSet = set()
	if N == 1:
		numSet.add(0)
	for i in range(10 ** (N-1), 10 ** N):
		addToSet = True
		num = str(i)
		for j in range(len(num) - 1):
			if abs(int(num[j]) - int(num[j+1])) != K:
				addToSet = False
				break
		if addToSet:
			numSet.add(i)
	return list(numSet)


def numsSameConsecDiffFast(N, K):
	bag = set()
	if N == 1:
		for i in range(0, 10):
			bag.add(i)
		return list(bag)
	for i in range(1, 10):
		generateNum(N, K, i, 0, '', bag)
	return list(bag)
	

def generateNum(N, K, i, posi, num, bag):
	if posi == N:
		bag.add(int(num))
		return
	num += str(i)
	if i+K >=0 and i+K < 10:
		generateNum(N, K, i+K, posi+1, num, bag)
	if i-K >=0 and i-K < 10:
		generateNum(N, K, i-K, posi+1, num, bag)


def main():
	str = input('input: ')
	N, K = str.split()
	output = numsSameConsecDiff(int(N), int(K))
	output2 = numsSameConsecDiffFast(int(N), int(K))
	print('output: ', output)
	print('output2: ', output2)


if __name__ == '__main__':
    main()