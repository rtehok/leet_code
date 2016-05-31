def solution(n): 
	arr = [1]*n
	if n > 2:
		for i in range(1,n):
			for x in range(i,n,i+1):
				arr[x] ^= 1
	elif n > 0:
		return 1
	else:
		return 0
	return sum(arr)
	
if __name__ == "__main__":
	print(solution(0))	
	print(solution(1))
	print(solution(2))
	print(solution(3))
	print(solution(4))
	print(solution(5))
	print(solution(6))
	print(solution(10))
	print(solution(999999))