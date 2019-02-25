class Node:


	def __init__(self, data=None):

		self.data = data
		self.next = None


	def __str__(self):

		if self.data is None and self.next is None:
			return "null"

		n_str = f"{self.data}"

		return n_str



class LinkedList(Node):


	def __init__(self, head=None):

		if head is not None:
			self.head = Node(head)
		else:
			self.head = None


	def append_to_tail(self, data_new):

		node_end = Node(data_new)

		if self.head is None:
			self.head = node_end
			return

		node_current = self.head
		while node_current.next is not None:
			node_current = node_current.next

		node_current.next = node_end


	def delete_node(self, n):

		if self.head is None:
			return

		if self.head.data == n:
			self.head = self.head.next
			return

		node_current = self.head
		while node_current.next is not None:
			if node_current.next.data == n:
				node_current.next = node_current.next.next
				break
			node_current = node_current.next


	def __str__(self):

		if self.head is None:
			return "[empty]"

		ll_str_list = []

		node_current = self.head

		while node_current is not None:
			ll_str_list.append(str(node_current))
			node_current = node_current.next

		ll_str = ")->(".join(ll_str_list)
		ll_str = f"({ll_str})"

		return ll_str



class Stack(LinkedList):

	
	def pop(self):

		if self.head is None:
			return None

		else:
			head = self.head
			self.head = self.head.next
			return head


	def push(self, n):

		if n is None:
			return

		new_node = Node(n)
		new_node.next, self.head = self.head, new_node


	def peek(self):

		return self.head


class Queue(LinkedList):

	def __init__(self, *args, **kwargs):
		
		super(Queue, self).__init__(*args, **kwargs)
		self.first = None
		self.last = None


	def enqueue(self, n):

		if self.last is None:
			self.last = Node(n)
			self.first = self.last

		else:
			self.last.next = Node(n)
			self.last = self.last.next


	def dequeue(self):

		if self.first is None:
			return

		tmp = self.first
		self.first = self.first.next

		return tmp.data



if __name__ == "__main__":

	a = Queue()

	a.enqueue(1)

	print(a)

