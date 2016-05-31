def main(num):
	pow = 1
	p = 1
	arr = [0]*(num+1)
	for i in range(1,num+1):
		if i == int(pow):
			arr[i] = 1
			pow = pow << 1
			p = 1
		else:
			arr[i] = arr[p] + 1
			p += 1
	print(arr)
		
if __name__ == "__main__":
	num = 5
	main(num)