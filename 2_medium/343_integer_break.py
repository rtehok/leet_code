import math

class Solution(object):
	#Dynamic programing
	def calc(n):
		if n <= 3:
			return n-1
		records = [0]*(n+1)
		records[1] = 1
		
		for i in range(2,n+1):
			for j in range(1,i):
				records[i] = max(records[i], ( j * ( max(i-j,records[i-j]) ) ) )
		return records
		
	#Mathematical solution
	def integerBreak(n):
		if n <= 3:
			return n-1
		elif n == 4:
			return 4
		prod = 1
		while (n > 4):
			prod *= 3
			n -= 3
			
		return prod*n
		
if __name__ == "__main__":
	for i in range(1,30):
		print(i,Solution.integerBreak(i))
	for i in range(1,30):
		print(i,Solution.calc(i))
	