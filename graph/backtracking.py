"""
Backtracking
https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf
"""

def perms(input_str):
	"""
	Classic exhaustive permutation pattern
	Forms all possible re-arrangements of the letters in a string.
	It is an example of an exhaustive procedural algorithm.
	"""

	def _perm(sofar, rest):
		"""
		if no more rest: add sofar to solution
		for every element of rest,
			recursively add all the permutation of sofar + element of rest
		"""
		nonlocal solutions

		if rest == "":
			solutions.append(sofar)
			return

		for i in range(len(rest)):
			str_remaining = rest[:i] + rest[i+1:]
			_perm(sofar + rest[i], str_remaining)

	solutions = []
	_perm("", input_str)

	return solutions


def subsets(input_set):
	"""
	Classic exhaustive subset pattern:
	-> listing all the subsets of a given set
	"""

	def _subset(sofar, rest):
		"""
		if rest is empty: add sofar to output subsets
		else:
			take next element of remaining:
				try adding it to subset of sofar using recursion
				try not adding it to subset of sofar using recursion
		"""
		nonlocal solutions

		if len(rest) == 0:
			solutions.append(sofar)

		else:
			next_element, rest = rest[0], rest[1:]
			_subset(sofar + next_element, rest)
			_subset(sofar, rest)

	solutions = []
	_subset(sofar=[], rest=input_set)
	return solutions


backtracking = """
	Backtracking...
	Instead of exploring exhaustively for all possibilities that work;
	we try one choice and only undo that decision doesn't work out
	---
	//BASE CASE: Reached end state, is it goal state?
	// TRY ALL AVAILABLE CHOICES
		//IF ANY WORK OUT: TRUE
		//IF NOT WORK OUT: BACKTRACK (UNDO)
	//TRY ALL CHOICES AND NONE WORKED OUT: FALSE
	---

	def solve(configs):

		if no more choice:
			return (conf is goal state)  // BASE CASE

		for c in choices:

			try choice c;
			OK = solve(conf with c);
			
			if OK:
				return True
			else:
				unmake choice c;

		return False
	"""


def find_word(sofar, rest, lexicon):
	"""
	Take a string of ch and rearrange it into valid word (in lexicon)
	"""
	if len(rest) == 0:
		return sofar if sofar in lexicon else ""

	for i in range(len(rest)):

		# optimization:
		# if new prefix is not a valid prefix as per lexicon: skip
		prefix = sofar + rest[i]
		valid_prefix = any([ w[:len(prefix)] == prefix for w in lexicon ])
		if not valid_prefix:
			continue 

		sofar += rest[i]
		rest = rest[:i] + rest[i+1:]

		res = find_word(sofar, rest, lexicon)

		if res != "":
			return res

		else:
			rest = sofar[-1] + rest
			sofar = sofar[:-1]

	return ""




def solve_8_queens():
	"""
	Objective
	------------------
	Assign eight queens to eight positions onan 8x8 chessboard so that no queen,
	according to the rules of normal chess play, can attack any other queen on the board
	------------------


	Algo:
	------------------
	Start in the leftmost columm
	
	If all queens are placed, return true

	for (every possible choice among the rows in this column)
		if the queen can be placed safely there,
		make that choice and then recursively try to place the rest of the queens

		if recursion successful, return true
		if !successful, remove queen and try another row in this column

	if all rows have been tried and nothing worked,
	return false to trigger backtracking
	------------------

	Functions
	------------------
	place_queen()
	remove_queen()
	is_safe()
	solve()
	------------------
	"""

class Board:

	def __init__(self, size):

		self.queens = []
		self.size = size


	def is_safe(self, target):

		row, col = target
		for r, c in self.queens:
			if r == row:
				return False
			if c == col:
				return False
			if (row - r) / (col - c) in (1, -1):
				return False
		return True 


	def remove_queen(self, target):

		self.queens.remove(target)


	def place_queen(self, target):

		self.queens.append(target)


class Solution:
	
	def __init__(self, size):

		self.size = size
		self.board = Board(size)
		self.solutions = []
		self.solve()


	def solve(self):

		row_i = len(self.board.queens)

		if row_i == self.size:
			self.solutions.append(self.board.queens)
			return True

		else:
			for col_i in range(self.size):
				target = (row_i, col_i)
				if self.board.is_safe(target):
					self.board.place_queen(target)
					if self.solve():
						return True
					else:
						self.board.remove_queen(target)
			return False



S = Solution(8)
print(S.solutions)



