from functools import reduce

def solution(nums):
	n = len(nums)
	res = [1] * n
	l = r = 1
	
	for i in range(1, n):
		l *= nums[i - 1]
		res[i] *= l
	
	for i in range(n - 2, -1, -1):
		r *= nums[i + 1]
		res[i] *= r
	
	return res
	
if __name__ == "__main__":
	print(solution([0,0]))
	print(solution([1,2,3,4]))
	print(solution([2,4,3,1]))