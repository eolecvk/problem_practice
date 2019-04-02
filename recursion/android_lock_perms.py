"""
Count Android lock permutations (size from 1 to 9)
Solution for permutation with repetition
"""

class Solution:


	def __init__(self):
		self.memo = {}


	def count_paths(self, pos, n_left):

		if n_left == 0:
			return 1

		if (pos, n_left) in self.memo:
			return self.memo[(pos, n_left)]

		else:
			if pos == "corner":
				ret = sum([
					4 * self.count_paths("side", n_left-1),
					1 * self.count_paths("mid", n_left-1)
					])
				
			elif pos == "side":
				ret = sum([
					2 * self.count_paths("side", n_left-1),
					4 * self.count_paths("corner", n_left-1),
					1 * self.count_paths("mid", n_left-1)
					])

			else:
				ret = sum([
					4 * self.count_paths("side", n_left-1),
					4 * self.count_paths("corner", n_left-1),
					])

			self.memo[(pos, n_left)] = ret
			return self.memo[(pos, n_left)]


	def numberOfPatterns(self, m, n):

		ret = 0
		for i in range(m, n+1):
			print(i)
			ret += sum([
				4 * self.count_paths("corner", i-1),
				1 * self.count_paths("mid", i-1),
				4 * self.count_paths("side", i-1) ])

		return ret
			

if __name__ == "__main__":

	m = 1
	n = 2

	S = Solution()
	print(S.numberOfPatterns(m, n))
