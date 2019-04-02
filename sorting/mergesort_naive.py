
def merge(sorted_a, sorted_b):

	sorted_ret = [None] * (len(sorted_a) + len(sorted_b))

	cur_a = 0
	cur_b = 0

	cur_r = 0

	while True:

		if cur_a == len(sorted_a):
			sorted_ret[cur_r:] = sorted_b[cur_b:]
			break

		elif cur_b == len(sorted_b):
			sorted_ret[cur_r:] = sorted_a[cur_a:]
			break
		
		if sorted_a[cur_a] < sorted_b[cur_b]:
			sorted_ret[cur_r] = sorted_a[cur_a]
			cur_a += 1
			cur_r += 1
			continue

		else:
			sorted_ret[cur_r] = sorted_b[cur_b]
			cur_b += 1
			cur_r += 1
			continue

	return sorted_ret


def mergesort(unsorted_list):

	if len(unsorted_list) <= 1:
		return unsorted_list

	else:
		mid_i = len(unsorted_list) // 2
		return merge(
			mergesort(unsorted_list[:mid_i]),
			mergesort(unsorted_list[mid_i:]))
	





if __name__ == "__main__":

	items = [1, 2, 1, 3, 1, 2, 4, 2]
	items_sorted = mergesort(items)
	print(items_sorted) 

