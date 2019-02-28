

def count_print_lines_test(tests):

	from palindrom_substrings import Line

	for entry in tests:

		line = entry["line"]

		print(line)

		is_valid_actual = entry["is_valid"]
		is_valid_pred = Line(line.rstrip()).is_valid()

		if is_valid_pred != is_valid_actual:
			print(f"Error; found line {line} : predicted -> {is_valid_pred}")
			return

		else:
			print(f"Passed; {is_valid_actual}")

		print()

	print("All tests passed")
#---


if __name__ == "__main__":

	tests = [
	{
		"line" : "fewwwwwwwwwwwef",
		"is_valid" : False
	},
	{
		"line" : "lool",
		"is_valid" : True
	},
	{
		"line" : "lool[lool]",
		"is_valid" : False
	},
	{
		"line" : "loole",
		"is_valid" : True
	},
	{
		"line" : "[lool",
		"is_valid" : True
	},
	{
		"line" : "lool]",
		"is_valid" : True
	},
	{
		"line" : "[[lool]woow]",
		"is_valid" : False
	},
	{
		"line" : "[woow]lool]",
		"is_valid" : False
	},
	{
		"line" : "rttr[mnop]qrst",
		"is_valid" : True

	},
	{
		"line" : "efgh[baab]ommo",
		"is_valid" : False
	},
	{
		"line" : "bbbb[qwer]ereq",
		"is_valid" : False
	},
	{
		"line" : "irttrj[asdfgh]zxcvbn",
		"is_valid" : True
	}
	]

	count_print_lines_test(tests)