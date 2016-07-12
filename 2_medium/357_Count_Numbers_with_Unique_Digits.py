class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n < 2:
			return 10**n
		res = [0] * (n+1)
		res[0] = [x for x in range(1,10)]
		res[1] = [x*11 for x in range(1,10)]
		for i in range(2,n+1):
			res[i] = set()
			for x in range(1,10):
				for j in res[i-1]:
					if x*(10**i) + j < 10**n:
						res[i].add( x*(10**i) + j )
					if j*(10**(i-1)) + x < 10**n:
						res[i].add( j*(10**(i-1)) + x )
		
		print(res[n-1])
		return 10**n - len(res[n-1])
		
		
if __name__ == "__main__":
	s = Solution()
	print(s.countNumbersWithUniqueDigits(0))
	print(s.countNumbersWithUniqueDigits(1))
	print(s.countNumbersWithUniqueDigits(2))
	print(s.countNumbersWithUniqueDigits(3))
	# print(s.countNumbersWithUniqueDigits(4))
	# print(s.countNumbersWithUniqueDigits(5))