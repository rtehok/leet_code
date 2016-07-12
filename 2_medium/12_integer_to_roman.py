class Solution(object):
	def intToRoman(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		tmp = []
		DICT = {1:'IV',2:'XL',3:'CD',4:'Mx'}
		res = ""
		for i,s in enumerate(str(num)):
			s = int(s)
			j = len(str(num)) - i
			one = DICT[j][0]
			five = DICT[j][1]
			if s < 4:
				res += one * s
			elif s == 4:
				res += DICT[j]
			elif s == 5:
				res += five
			elif s > 5 and s < 9:
				res += five + (s-5) * one
			else:
				 res += one + DICT[j+1][0]
		
		return res
		
if __name__ == "__main__":
	s = Solution()
	for i in range(3000,4000):
		print(i,s.intToRoman(i))