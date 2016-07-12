class Node(object):
	def __init__(self,val=None):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		# return max(self.func(root))
		return self.func(root)[0]
		
	def func(self,root):
		if not root:
			return (0,0)
		else:
			# print(root.val)
			# s = self.func(root.left)[1] + self.func(root.right)[1]
			# m = self.func(root.left)[0] + self.func(root.right)[0] + root.val
			# print(s,m)
			rob_l, no_rob_l = self.func(root.left)
			rob_r, no_rob_r = self.func(root.right)
		return max(no_rob_l + no_rob_r + root.val, rob_l + rob_r), rob_l + rob_r
		
		
if __name__ == "__main__":
	s = Solution()
	root = Node(3)
	root.left = Node(2)
	root.right = Node(3)
	two = root.left
	two.left = Node(3)
	three = root.right
	three.left = Node(1)
	print(s.rob(root))
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	two = root.left
	two.left = Node(4)
	two.right = Node(5)
	print(s.rob(root))
	root = Node(3)
	root.left = Node(4)
	root.right = Node(5)
	four = root.left
	four.left = Node(1)
	four.right = Node(3)
	five = root.right
	five.left = Node(1)
	print(s.rob(root))
	root = Node(2)
	root.left = Node(1)
	root.right = Node(3)
	one = root.left
	one.left = Node(4)
	print(s.rob(root))