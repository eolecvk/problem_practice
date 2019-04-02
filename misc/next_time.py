"""
Next closest time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.
You may assume the given input string is always valid.
For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
"""


def next_time(time_str):

	hour, minute = time_str.split(":")
	        
	# Generate all possible 2 digit values
	# There are at most 16 sorted values here
	nums = sorted(set(hour + minute))
	two_digit_values = [a+b for a in nums for b in nums]

	# Check if the next valid minute is in the hour
	i = two_digit_values.index(minute)
	if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "60":
		return f"{hour}:{minutes_next[0]}"

	# Check if the next valid hour is in the day
	i = two_digit_values.index(hour)
	if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "24":
		return f"{hours_next[0]}:{two_digit_values[0]}"

	# Return earliest time in the day
	return f"{two_digit_values[0]}:{two_digit_values[0]}"

print(next_time("19:33"))
