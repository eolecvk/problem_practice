

class BST:

	def __init__(self, key):

		self.data = key
		self.left = None
		self.right = None	


	def search(self, key):

		if self is None:
			return self

		elif self.data == key:
			return self

		elif key <= self.data:
			return self.left.search(key)

		else:
			return self.right.search(key)


	def insert(self, key):

		if self is None:
			self.data = key
			self.right = None
			self.left = None

		elif key <= self.data:
			if self.left is None:
				self.left = BST(key)
			else:
				self.left.insert(key)

		else:
			if self.right is None:
				self.right = BST(key)
			else:
				self.right.insert(key)


	def delete(self, key):

		def find_min(self):

			current_node = self
			while current_node.left is not None:
				current_node = current_node.left

			return current_node
		#---

		if self is None:
			return self

		if self.data <= key:
			self.left = delete(self.left, key)

		elif self.data > key:
			self.right = delete(self.right, key)

		else:
			# node deleted is a leaf 
			if self.left is None and self.right is None:
				return None

			# or has at most one child
			elif self.left is not None:
				tmp = self.left
				self = None
				return tmp

			elif self.right is not None:
				tmp = self.right
				self = None
				return tmp

			# node deleted has two children
			else:

				# find in-order successor
				in_order_successor = find_min(self.right)

				# replace value of node with value of inOrderSuccessor
				self.data = in_order_successor.data

				# delete inOrderSuccessor
				delete(self, in_order_successor)



	def get_height(self):

		if self.right is None and self.left is None:
			return 0
		else:
			return 1 + max([get_depth(self.right), get_depth(self.left)])








# def AVLT(BST):

# 	def balance(self)

if __name__ == "__main__":

	b = BST(0)

	for el in range(1, 2):
		b.insert(el)

	for el in range(-1, -2, -1):
		b.insert(e)l

	print(b)
