
import numpy as np
import random


class TrieNode:

	def __init__(self):
		self.is_word = False
		self.children = {}


class Trie:

	def __init__(self):
		self.root = TrieNode()


	def insert(self, word):

		node = self.root
		for ch in word:
			if ch not in node.children:
				node.children[ch] = TrieNode()
			node = node.children[ch]
		node.is_word = True


	def search(self, word):

		node = self.root
		for ch in word:
			if ch not in node.children:
				return False
			node = node.children[ch]
		return node.is_word


	def startsWith(self, prefix):

		node=self.root
		for ch in prefix:
			if ch not in node.children:
				return False
			node = node.children[ch]
		return True


	def __str__(self):

		def find_words(root, prefix):

			words = []
			if root.is_word:
				words.append(prefix)

			for ch in root.children:
				words.extend(find_words(root.children[ch], prefix=prefix+ch))

			return words
		#---

		return ", ".join(find_words(self.root, prefix=""))
		


class Boggle:

	def __init__(self, shape=(10, 10)):

		flat_values = [ chr(random.choice( range(ord('a'), 26 + ord('a')) )) for _ in range(shape[0] * shape[1])]

		self.grid = np.matrix(flat_values)
		self.grid = self.grid.reshape(shape)
		self.shape = shape


	def get_value(self, position):

		return self.grid[position]


	def find_all_words(self, trie):


		def list_adjactent_moves(current_move):

			return (
				(current_move[0] + 1, current_move[1]    ),
				(current_move[0] - 1, current_move[1]    ),
				(current_move[0]    , current_move[1] + 1),
				(current_move[0]    , current_move[1] - 1)
				)


		def is_valid(move):

			return (
				move[0] > 0             and
				move[0] > 0             and
				move[0] < self.grid.shape[0] and
				move[1] < self.grid.shape[1] )


		def is_unvisited(move, visited):

			return move not in visited


		def get_valid_next_moves(position, visited):

			return [
				move for move in list_adjactent_moves(position)
				if is_valid(move) and is_unvisited(move, visited) ]


		def dfs(prefix, position, visited, trie):

			nonlocal words_found

			ch = self.get_value(position)
			visited.append(position)
			prefix += ch

			if ch in trie.children:

				trie = trie.children[ch]

				if trie.is_word:
					words_found.append(prefix)

				for move in get_valid_next_moves(position, visited):
					dfs(prefix, move, visited, trie)
		#----

		words_found = []

		for i in range(self.shape[0]):

			for j in range(self.shape[1]):

				dfs(prefix="", position=(i, j), visited=[], trie=trie.root)

		return set(words_found)


	def __str__(self):

		return str(self.grid)






if __name__ == "__main__":

	# prepare tie for lookup

	# load english dictionary
	import os 
	dir_path = os.path.dirname(os.path.realpath(__file__))
	fpath = f"{dir_path}/word_list.csv"

	import csv
	with open(fpath, 'r') as fp:
		words_list = list(csv.reader(fp))[0]

	# insert all words to a trie
	trie = Trie()
	for word in words_list:
		trie.insert(word)

	# initialize boggle grid
	boggle = Boggle()

	print(boggle)

	# find all words
	print(boggle.find_all_words(trie))