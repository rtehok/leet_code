class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		res = []
		
		if numRows >= 1:
			res.insert(0,[1])
			tmp = res[0]
			while len(tmp) < numRows:
				tmp = [1] + [ res[-1][i-1] + res[-1][i] for i in range(1,len(res[-1])) ] + [1]
				res.append(tmp)
		return res
		
if __name__ == "__main__":
	s = Solution()
	print(s.generate(5))