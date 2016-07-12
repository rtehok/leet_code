class Solution(object):
	def maxProduct(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""
		m = 0
		sub = [ (set(x),len(x)) for x in words ]
		for i in range(len(sub)):
			for j,next_word in enumerate(sub[i:]):
				has_common_letter = False
				for w in sub[i][0]:
					if w in next_word[0]:
						has_common_letter = True
						break
				if not(has_common_letter) and sub[i][1] * sub[j+i][1] > m:
					m = sub[i][1] * sub[j+i][1]
		return m

if __name__=="__main__":
	with open('./318_Maximum_Product_of_Word_Lengths.txt','r') as f:
		for line in f:
			s = Solution()
			l = [ x.strip(' "\'\t\r\n') for x in list(line[1:-1].split(","))]
			print(l)
			print(s.maxProduct(l))