class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# return self.helperClimbStairs(n,0)
			
	# def helperClimbStairs(self,n,s):
		# if s == n :
			# return 1
		# elif s > n:
			# return 0
		
		# res = 0
		
		# for j in range(1,3):
			# res += self.helperClimbStairs(n,s+j)
				
		# return res
		dp = [0] * (n + 1)
		dp[0] = dp[1] = 1
		
		for i in range(2, n + 1):
			dp[i] = dp[i - 1] + dp[i - 2]
			
		return dp[n]
		
if __name__ == "__main__":
	s = Solution()
	print(s.climbStairs(4))
	print(s.climbStairs(35)) #14930352
	