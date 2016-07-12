class Solution(object):
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		res = []
		tmp = []
		res.append(self.helper(n,k,res,tmp,1))
		return res
		
	def helper(self,n,k,res,tmp,cur):
		if len(tmp) == k:
			res.append(tmp[:])
			return
			
		for i in range(cur,n+1):
			tmp.append(i)
			self.helper(n,k,res,tmp,i+1)
			tmp.pop()
		
if __name__ == "__main__":
	s = Solution()
	print(s.combine(4,3))