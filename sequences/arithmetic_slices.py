"""
Arithmetic Slices
A sequence of number is called arithmetic
if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

The function should return the number of arithmetic slices in the array A. 
"""


def brute_force(array):
	"""
	Iteratively consider every 3 consecurive elements:
		if they are slices,
		iteratively add element to the right hand side
		for as long as they remain slices
	"""

	count = 0

	for i in range(len(array[:-2])):
		c = array[i+1] - array[i]

		if array[i+2] - array[i+1] == c:
			count += 1
			print(array[i:i+3])
		else:
			continue

		for j in range(i+3, len(array)):
			if array[j] - array[j-1] == c:
				count += 1
				print(array[i:j+1])
			else:
				break

	return count



def dynamic_programming(array):
	"""
	Considering that the number of sequences that ends at a given index i in an array A
	Is equal to:
		1 + (number of sequences that end at i - 1)
			if A[i] - A[i-1] == A[i-1] - A[i-2]
		0 
			otherwise
	We can use DP to efficiently count for each index,
	the number of arithmetic sequences that ends at given index.
	Since these sequences constitute exclusive sets (a sequence cannot end at 2 difference indices)
	we obtain the total number of arithmetic sequences in A by summing up
	the counts of arithmetic sequences ending at each possible index.
	"""
	if len(array) < 3:
		return 0

	count_current = 0 # tracks # of arithmetic seq ending and index i
	count_total = 0 # tracks total # of of arithmetic seq betweet 0 and i

	for i in range(2, len(array)):

		if array[i] - array[i - 1] == array[i - 1] - array[i - 2]:
			count_current += 1
		else:
			count_current = 0
		
		count_total += count_current

	return count_total






if __name__ == "__main__":

	seq = [1, 1, 1, 2, 3, 4, 1, 0, -1, -2]
	print(brute_force(seq))
	print(dynamic_programming(seq))
