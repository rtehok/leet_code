class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		L = len(nums)
		arr1 = [0] * (L + 1)
		arr2 = [0] * L
		if L == 0: return 0
		if L == 1: 
			return nums[0]
		elif L > 1:
			arr1[1] = nums[0]
			arr2[1] = nums[1]
			for i in range(2,L+1):
				if nums[i-1] + arr1[i-2] > arr1[i-1]:
					arr1[i] = nums[i-1] + arr1[i-2]
				else:
					arr1[i] = arr1[i-1]
				if i < L:
					if nums[i] + arr2[i-2] > arr2[i-1]:
						arr2[i] = nums[i] + arr2[i-2]
					else:
						arr2[i] = arr2[i-1]
		print(arr1,arr2)
		return max(arr1[-2],arr2[-1])
		
if __name__ == "__main__":
	s = Solution()
	print(s.rob([10,1,2,4,8]))
	print(s.rob([10,1,1,2,1,4]))
	print(s.rob([1,2,1,1]))
	print(s.rob([1,1,1,2]))