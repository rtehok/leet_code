class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		
		res = []
		
		def helper(candidates,target,current,tmp):
			if current == 0:
				res.append(tmp[:])
				return
			
			for i in candidates:
				if i <= current:
					tmp.append(i)
					helper(candidates,target,current - i,tmp)
					tmp.pop()
					
		helper(candidates,target,target,[])
		
		return res
		
if __name__ == "__main__":
	s = Solution()
	print(s.combinationSum([2,3,6,7],17))