"""
a topological sort or topological ordering of a directed graph is a linear ordering of its vertices
such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

The canonical application of topological sorting is in scheduling a sequence of jobs or tasks based on their dependencies.
"""



def topological_sort_kahn(graph, n):
    """
    Kahn's algorithm:
    Choose vertices in the same order as the eventual topological sort.
    First, find a list of "start nodes" which have no incoming edges and insert them into a set S;
    at least one such node must exist in a non-empty acyclic graph. Then:

    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edge
    while S is non-empty do
        remove a node n from S
        add n to tail of L

        for each node m with an edge e from n to m do
            remove edge e from the graph
            if m has no other incoming edges then
                insert m into S

    if graph has edges then
        return error   (graph has at least one cycle)
    else 
        return L  (a topologically sorted order)
    """

    # Ini topologically sorted list of vertices
    L = []

    # Find start vertices (ie no incoming edges)
    S = [
            i for i in range(n)
            if not any([i == e[1] for e in graph])
        ]

    # While S not empty
    while S:
        start_node = S.pop()
        L.append(start_node)

        # For all node m such that there is an edge (nm)
        for edge in [edge for edge in graph if edge[0] == start_node]:
            end_node = edge[1]

            # remove edge e from the graph
            graph.remove(edge)

            # if m has no other incoming edge, add m to S
            if not any([e for e in graph if e[1]==end_node]):
                S.append(end_node)

    # If graph has edges then it means graph has at least one cycle -> return Error
    if graph:
        raise ValueError("Graph has a cycle")
    else:
        return L



def topological_sort_DFS(graph, n):
    """
    Loops through each node of the graph, in an arbitrary order,
    initiating a depth-first search that terminates when it hits any node that has already been visited
    since the beginning of the topological sort or the node has no outgoing edges (i.e. a leaf node)

    L ← Empty list that will contain the sorted nodes
    while there are unmarked nodes do
        select an unmarked node n
        visit(n)

    function visit(node n)
        if n has a permanent mark then return
        if n has a temporary mark then stop   (not a DAG)
        mark n temporarily
        for each node m with an edge from n to m do
            visit(m)
        mark n permanently
        add n to head of L
    """

    def visit(node, visited_tmp=[]):
        nonlocal visited
        nonlocal L

        if node in visited:
            return

        if node in visited_tmp:
            raise ValueError("Graph has cycle!")

        visited_tmp.append(node)
        outgoing_edges = [e for e in graph if e[0] == node]

        for outgoing_edge in outgoing_edges:
            node_e = outgoing_edge[1]
            visit(node_e, visited_tmp)

        visited.append(node)
        L = [node] + L
    #---

    # Topologically sorted list of vertices
    L = []

    # List of visited nodes
    unvisited = [i for i in range(n)]
    visited = []

    # DFS
    while unvisited:
        node = unvisited.pop()
        visit(node, visited_tmp=[])

    return L



def shortest_path(V, s, graph):
    """
    @param, V : list of vertices in topological order
    @param, s : source node to finding all shortest path from

    Using topological sorting of V
    for shortest path finding from a source vertex to all other vertices in the graph
    ---

    Let d be an array of the same length as V;
    this will hold the shortest-path distances from s. Set d[s] = 0, all other d[u] = ∞.
    
    Let p be an array of the same length as V,
    with all elements initialized to nil.
    Each p[u] will hold the predecessor of u in the shortest path from s to u.
    
    Loop over the vertices u as ordered in V, starting from s:
        For each vertex v directly following u (i.e., there exists an edge from u to v):
            Let w be the weight of the edge from u to v.
            Relax the edge: if d[v] > d[u] + w, set
                d[v] ← d[u] + w,
                p[v] ← u.


    """

    # Container for all shortest path dist from s to all nodes i
    d = [1000] * len(V)
    d[s] = 0

    # Container for all predecessor to node i in shortest path from s to i
    p = [None] * len(V)

    # Iterate over nodes in topological order, starting from source
    for node in V[V.index(s):]:
        for outgoing_edge in [e for e in graph if e[0] == node]:
            outgoing_edge_weight = 1
            node_next = outgoing_edge[1]

            # Relax edge
            if d[node_next] > d[node] + outgoing_edge_weight:
                d[node_next] = d[node] + outgoing_edge_weight
                p[node_next] = node








if __name__ == "__main__":

    graph = [
        [5, 0],
        [4, 0],
        [4, 1],
        [3, 1],
        [2, 3],
        [5, 2]
    ]

    n = 6

    #L = topological_sort_kahn(graph, n)
    #print(L)


    L = topological_sort_DFS(graph, n)
    print(L)

    
