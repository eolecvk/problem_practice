
new_generator = (x**2 for x in [1, 2, 3])
next(new_generator)
next(new_generator)


def finbon_gen(n):

	a = b = 1

	for i in range(n):
		yield a
		a, b = b, a + b