class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		
		arr = [ord(x) - 64 for x in s]
		res = 0
		for i,v in enumerate(arr):
			res = res * 26 + arr[i]
			
		return(res)
		
if __name__ == "__main__":
	s = Solution()
	print(s.titleToNumber('A'))
	print(s.titleToNumber('Z'))
	print(s.titleToNumber('AB'))
	print(s.titleToNumber('BA'))
	print(s.titleToNumber('ZZ'))
	print(s.titleToNumber('XX'))
	print(s.titleToNumber('AAA'))