
# flood fill
# given a multi-dimensional array of integers
# given a start node and a replacement value, looks for all nodes in the array that are connected to the start node by a valid path and change their value to the replacement value.
# A path is valid iif each node in the path has a value equal to the start node and if it is adjacent to another node in the path or to the start node.

import numpy as np
import random

class Grid:
	
	def __init__(self, shape=(10, 10)):

		self.grid = np.multiply(np.random.rand(*shape), 10).astype(int) % 3
		self.shape = shape


	def get_value(self, position):

		return self.grid[position]


	def set_value(self, position, value):

		self.grid[position] = value


	def __str__(self):

		return str(self.grid)




def get_valid_neighbors(start_node, reference_value):


	def adjacent_nodes(ref_node):

		adjacent_nodes = [
			(ref_node[0] + 1, ref_node[1]    ),
			(ref_node[0] - 1, ref_node[1]    ),
			(ref_node[0]    , ref_node[1] + 1),
			(ref_node[0]    , ref_node[1] - 1) ]

		adjacent_nodes = [ node for node in adjacent_nodes
						   if all([
							node[0] >= 0,
							node[1] >= 0,
							node[0] < grid.shape[0],
							node[1] < grid.shape[1] ]) ]

		return adjacent_nodes


	def has_reference_value(node, reference_value):

		node_value = grid.get_value(node)
		return node_value == reference_value

	#---

	valid_neighbors = [
		node for node in adjacent_nodes(start_node)
		if has_reference_value(node, reference_value) ]

	return valid_neighbors



def flood_fill(grid, start_node, new_value):

	reference_value = grid.get_value(start_node)
	
	visited = [start_node]

	stack = [start_node]

	while stack:

		current_node = stack.pop()
		grid.set_value(current_node, new_value)

		for valid_neighbor in get_valid_neighbors(current_node, reference_value):
			if valid_neighbor not in visited:
				stack.append(valid_neighbor)

	return grid




if __name__ == "__main__":


	g = Grid()

	print(g)

	pos1 = int(input("row_num "))
	pos2 = int(input("col_num "))
	new_val = int(input("new value "))

	flood_fill(g, start_node=(pos1, pos2), new_value=new_val)

	print(g)


