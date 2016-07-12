class Solution(object):
	def generateParenthesis(self, n):
		result = []
		result = self.generate_parenthesis(0, 0, n, '', result)
		return result


	def generate_parenthesis(self, open_num, close_num, maximum, combi, result):
		# Base case: because we add close only if close_num < open_num, once 
		# close_num hits maximum (n), we want to stop
		if close_num == maximum:
			result.append(combi)
			return

		# The only constraint for adding open parenthesis is the max number of 
		# parentheses (maximum)
		if open_num < maximum:
			print(open_num + 1,close_num, combi + '(')
			self.generate_parenthesis(open_num + 1, close_num, 
									  maximum, combi + '(', result)

		# We only add close parenthesis if there are enough open parentheses to close
		if close_num < open_num:
			print(open_num,close_num + 1, combi + ')')
			self.generate_parenthesis(open_num, close_num + 1, 
									  maximum, combi + ')', result)
									  
		return result
								  
if __name__ == "__main__":
	s = Solution()
	print(s.generateParenthesis(3))