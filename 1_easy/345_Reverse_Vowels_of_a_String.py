class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		VOWELS = ('a','e','i','o','u')
		if len(s) == 1 or s.strip() == "":
			return s
		else:
			i = 0
			j = len(s) - 1
			out = [''] * len(s)
			while i <= j:
				if s[i] not in VOWELS:
					out[i] = s[i]
					i += 1
				if s[j] not in VOWELS:
					out[j] = s[j]
					j -= 1
				if s[i] in VOWELS and s[j] in VOWELS:
					out[i] = str(s[j])
					out[j] = str(s[i])
					i += 1
					j -= 1
			return "".join(out)
			
if __name__ == "__main__":
	s = Solution()
	print(s.reverseVowels('hello'))
	print(s.reverseVowels('a.'))
	print(s.reverseVowels('!!!'))