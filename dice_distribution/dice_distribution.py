# credits Antoon Pardon
# https://bytes.com/topic/python/answers/476465-dice-probability-problem


import operator

class Distribution(dict):

	'''A distribution is a dictionary where the keys are dice
	totals and the values are the number of possible ways
	this total can come up '''

	def __add__(self, term):

	'''Take two distributions and combine them into one.'''

		result = Distribution()

		for k1, v1 in self.items():

			for k2, v2 in term.items():

				k3 = k1 + k2
				v3 = v1 * v2
				
				try:
					result[k3] += v3

				except KeyError:
					result[k3] = v3

		return result


	def __rmul__(self, num):

		tp = num * [self]

		return reduce(operator.add, tp)



def D(n):
	''' One die has a distribution where each result has
	one possible way of coming up '''
	return Distribution((i,1) for i in range(1,n+1))


if __name__ == "__main__":

	sum3d6 = 3 * D(6)
	sum2d6p2d4 = 2 * D(6) + 2 * D(4)