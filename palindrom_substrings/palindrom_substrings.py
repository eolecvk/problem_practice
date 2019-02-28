class Window:

	def __init__(self, window, depth):
		assert len(window) == 4, "window arg should be a list of len 4"
		self.window = window
		self.depth = depth

	def __str__(self):
		list_str = "".join(self.window)
		depth_str = f"{self.depth}"
		return  list_str + " " + depth_str

	def is_valid_palindrome(self):
		return all([
			self.window[0] == self.window[-1],
			self.window[1] == self.window[-2],
			self.window[0] != self.window[1] ])



class Valid_Windows_Stack:

	def __init__(self):
		self.items = []

	def __str__(self):
		return "\n\t".join([str(o) for o in self.items])

	def first_valid_window_str(self):
		if self.size == 0:
			return

		valid_window_0 = self.peek()
		return "".join(valid_window_0.window)

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		assert isinstance(item, Window), f"{item} is `{type(item)}`, not `Window`"
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def get_max_depth(self):
		if self.isEmpty:
			return

		window_max_depth = self.peek()
		max_depth = window_max_depth.depth
		return max_depth

	def remove_window_max_depth(self, depth_thresh):

		if self.isEmpty():
			return

		top_window = self.pop()

		if top_window.depth <= depth_thresh:
			self.push(top_window)
		else:
			#print(f"{''.join(top_window.window)} is in brackets") 
			self.remove_window_max_depth(depth_thresh)


class Line:

	def __init__(self, line_str):
		self.line = line_str

	def __len__(self):
		return len(self.line)

	def __str__(self):
		return str(self.line)

	def get_window(self, start_i):
		if len(self.line) < start_i + 4:
			return
		else:
			window = [self.line[i] for i in range(start_i, start_i + 4)]
			return window

	def is_valid(self):
		if len(self) < 4:
			return False

		valid_window_stack = Valid_Windows_Stack()
		open_brackets_count = 0

		for i in range(len(self.line)):

			window_end_i = i + 3

			if window_end_i < len(self.line):

				current_window = Window(
						window=self.get_window(i),
						depth=open_brackets_count)

				if current_window.is_valid_palindrome():
					valid_window_stack.push(current_window)

			if self.line[i] == '[':
				open_brackets_count += 1

			elif self.line[i] == ']':
				open_brackets_count = max(0, open_brackets_count-1)

				size_stack_before = valid_window_stack.size()
				valid_window_stack.remove_window_max_depth(open_brackets_count)
				size_stack_after = valid_window_stack.size()

				if size_stack_before != size_stack_after:
					return False
				

		if valid_window_stack.size() > 0:
			#valid_str = valid_window_stack.first_valid_window_str()
			#print(f"{valid_str} is out of brackets")
			return True

		return False

#---

def count_print_lines_txt(fpath):

	c = 0

	with open(fpath, 'r') as fp:
		for line in fp:
			new_line = Line(line.rstrip())
			if new_line.is_valid():
				print(new_line)
				c += 1

	return c



if __name__ == "__main__":

	fpath = "/home/eolus/Desktop/sample_strings.txt"
	c = count_print_lines_txt(fpath)

	print(f"\nNumber of valid lines: {c}")