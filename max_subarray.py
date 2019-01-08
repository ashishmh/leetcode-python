import sys

# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums, l, r):
	if l == r:
		return nums[l]

	m = int((l + r) / 2)
	leftMaxSum = maxSubArray(nums, l, m)
	rightMaxSum = maxSubArray(nums, m+1, r)
	
	lsum = (-sys.maxsize)
	sum = 0
	for i in range(m, -1, -1):
		sum += nums[i]
		lsum = max(sum, lsum)
	sum = 0
	rsum = (-sys.maxsize)
	for i in range(m + 1, r + 1):
		sum += nums[i]
		rsum = max(sum, rsum)
	crossSum = lsum + rsum
	return max(leftMaxSum, rightMaxSum, crossSum)


def maxSubArrayFast():
	


def main():
	str = input('input: ')
	nums = list(map(int, str.split(',')))
	output = maxSubArray(nums, 0, len(nums) - 1)
	print('output: ', output)


if __name__ == '__main__':
    main()