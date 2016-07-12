class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		for i in nums[:]:
			if i == val:
				nums.remove(i)
		return nums
		
if __name__ == "__main__":
	s = Solution()
	print(s.removeElement([2,2,3,4,2,3],3))