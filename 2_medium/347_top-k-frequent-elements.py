def solution(nums,k): 
	d = {}
	for x in nums:
		try:
			d[x]+=1
		except:
			d[x] = 1
	
	out = []
	for key,val in reversed(sorted(d.items(), key=lambda x:x[1])):
		if k == 0:
			break
		out.append(key)
		k -= 1
		
	return out
	
if __name__ == "__main__":
	nums = [1,1,1,2,2,3]
	k=2
	print(solution(nums,k))