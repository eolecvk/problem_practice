


class MergeSort:

	def __init__(self, input_array):
		"""
		Array A[] has the items to sort;
		array B[] is a work array.
		"""
		n = len(input_array)

		self.A = input_array
		self.B = [None] * n
		self.topdown_mergesort(n)

		self.sorted_array = self.A


	def copy_array(self, i_begin, i_end):
		"""
		Copy A[i_begin:i_end] into B[i_begin:i_end]
		"""
		self.B[i_begin:i_end] = self.A[i_begin:i_end]


	def topdown_mergesort(self, n):
		self.copy_array(0, n) # duplicate array A[] into B[]
		self.topdown_splitmerge(0, n) # sort data from B[] into A[]


	def topdown_splitmerge(self, i_begin, i_end):
		"""
		Sort the given run of array A[]
		using array B[] as a source.
		"""
		if i_end - i_begin <= 1:
			return

		else:
			i_mid = int((i_end + i_begin) / 2)
			print(i_begin, i_mid)
			print(i_mid, i_end)
			self.topdown_splitmerge(i_begin, i_mid)
			self.topdown_splitmerge(i_mid, i_end)
			self.topdown_merge(i_begin, i_mid, i_end)
			print(self.A[i_begin:i_end])


	def topdown_merge(self, i_begin, i_mid, i_end):

		i = i_begin
		j = i_mid

		for k in range(i_begin, i_end):
			if i < i_mid and (j >= i_end or self.A[i] <= self.A[j]):
				self.B[k] = self.A[i]
				i += 1
			else:
				self.B[k] = self.A[j]
				j += 1


if __name__ == "__main__":

	items = [1, 2, 3, 1, 2, 4, 1, 2]
	print(MergeSort(items).sorted_array) #???


			







