import math

class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		arr = [True] * n
		if n <= 2:
			return 0
		else:
			arr[0] = False
			arr[1] = False
			for i in range(2,int(math.sqrt(n))+1):
				if arr[i]:
					for j in range(i*i,n,i):
						arr[j] = False
			return sum([x for x in arr if x])
			
if __name__ == "__main__":
	s = Solution()
	print(s.countPrimes(15))
	print(s.countPrimes(5))
	print(s.countPrimes(7))