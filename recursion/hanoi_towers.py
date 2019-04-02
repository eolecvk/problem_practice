
from collections import deque


class Hanoi:

	def __init__(self, size):
		
		self.size = size
		self.src = deque()
		self.buf = deque()
		self.dst = deque()

		for i in range(size-1, -1, -1):
			self.src.append(i)


	def solve(self):
		self.move_tower(self.size, self.src, self.dst, self.buf)


	def move_disk(self, from_tower, to_tower):
		d = from_tower.pop()
		to_tower.append(d)


	def move_tower(self, n_disks, src_tower, dst_tower, buf_tower):
		if n_disks == 1:
			self.move_disk(
				from_tower=src_tower,
				to_tower=dst_tower)
		else:
			self.move_tower(
				n_disks=n_disks-1,
				src_tower=src_tower,
				dst_tower=buf_tower,
				buf_tower=dst_tower)
			self.move_tower(
				n_disks=1,
				src_tower=src_tower,
				dst_tower=dst_tower,
				buf_tower=buf_tower)
			self.move_tower(
				n_disks=n_disks-1,
				src_tower=buf_tower,
				dst_tower=dst_tower,
				buf_tower=src_tower)			



if __name__ == "__main__":

	H = Hanoi(4)
	print(H.src)
	print(H.buf)
	print(H.dst)


	H.solve()
	print(H.src)
	print(H.buf)
	print(H.dst)
