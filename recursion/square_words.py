"""
Given a set of words (without duplicates), find all word squares you can build from them.
For instance:

["ball","area","lead","lady"]

b a l l
a r e a
l e a d
l a d y

"""


def word_square(lexicon):

	def build_prefix_dict(words):
		"""
		Complete mapping between
		prefix -> list of full words
		"""
		from collections import defaultdict

		fulls = defaultdict(list)
		for word in words:
			for i in range(len(word)):
				fulls[word[:i]].append(word)

		return fulls


	def build_square(square):
		"""
		add full word with valid prefix
		from existing (incomplete) list of words
		until full square is formed
		"""

		if len(square)==max_size:
			squares.append(square)
			return

		else:
			prefix = "".join([w[len(square)] for w in square])
			for word in prefix_dict[prefix]:
				build_square(square + [word])


	squares = []
	max_size = len(lexicon[0])

	prefix_dict = build_prefix_dict(lexicon)
	
	for word in lexicon:
		build_square([word])

	return squares





if __name__ == "__main__":

	lex = ["area","lead","wall","lady","ball"]
	print(word_square(lex))




