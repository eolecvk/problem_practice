"""
Count connected components in an undirected graph
"""

def countComponents_dfs(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """

    components = { v : None for v in range(n) }
    
    def build_graph(edges, n):
        
        G = { i : [] for i in range(n) }
        
        for edge in edges:
            G[edge[0]].append(edge[1])
            G[edge[1]].append(edge[0])
        
        return G
    
    
    def DFS(vertex, component, G):
        
        if components[vertex] is not None:
            return
        
        components[vertex] = component
        
        for adj_vertex in G[vertex]:
            DFS(adj_vertex, component, G)
    
    #---

    G = build_graph(edges, n)
    
    for vertex, component in components.items():
        
        if component is None:
            DFS(vertex, vertex, G)
    
    return len(set(components.values()))




#====

class DisjointSet:

	def __init__(self):
		self.leader = {} # keep track of node -> leader refs
		self.group = {}  # keep track of leader->(set of nodes) refs

	def add(self, a, b):
		"""
		update leaders
		update groups
		so as to reflect that a and b are now connected (part of the same group)
		"""

		leader_a = self.leader.get(a)
		leader_b = self.leader.get(b)

		if not any([leader_a is None, leader_b is None]):
			
			# nothing to update
			if leader_a == leader_b:
				return

			if len(self.group.get(leader_a)) < len(self.group.leader_b):
				a, b = b, a
				leader_a, leader_b = leader_b, leader_a

			# update leader refs
			for n in self.group[leader_b]:
				self.leader[n] = leader_a
			# update group refs
			self.group[a] |= self.group[b]
			del self.group[b]


		elif all([leader_a is None, leader_b is None]):

			# update leader refs
			self.leader[b] = a
			self.leader[a] = a
			
			# update group refs
			self.group[a] = set([a, b])

		else:
			if leader_a is None:
				a, b = b, a
				leader_a, leader_b = leader_b, leader_a

			# update leader refs
			self.leader[b] = leader_a
			# update group refs
			self.group[leader_a].add(b)





def countComponents_disjointset_v1(n, edges):

	ds = DisjointSet()

	for edge in edges:
		vertex_a = edge[0]
		vertex_b = edge[1]
		ds.add(vertex_a, vertex_b)

	return len(ds.group)


def countComponents_unionset(n, edges):

	def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
        
    def union(xy):
        x, y = map(find, xy)
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    
    parent, rank = range(n), [0] * n
    map(union, edges)
    return len({find(x) for x in parent})





if __name__ == "__main__":

	edges = [[0, 1], [1, 1], [2, 3], [3, 4]]
	n = 5

	print(countComponents_disjointset(n, edges))