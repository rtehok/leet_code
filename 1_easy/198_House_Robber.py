class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# L=len(nums)
		# arr = [0]*(L+1)
		# if L >= 1: arr[1] = nums[0]
		# if L > 1:
			# for i in range(2,len(nums)+1):
				# if nums[i-1] + arr[i-2] > arr[i-1]:
					# arr[i] = nums[i-1] + arr[i-2]
				# else:
					# arr[i] = arr[i-1]
		# return arr[-1]
		L=len(nums)
		m1 = 0
		m2 = 0
		for rob in nums:
		    tmp = m1
		    m1 = max(m1,m2+rob)
		    m2 = tmp
		return m1
		
if __name__ == "__main__":
	s = Solution()
	print(s.rob([10,1,2,4,8]))
	print(s.rob([10,1,1,2,1,4]))