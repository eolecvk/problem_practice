"""
disjoint-set data structure
----

Motivation: find if two objects connect efficiently.


objects
0  1  2  3  4  5  6  7  8  9 # grid data points

disjoint sets of objects
0  1  { 2 3 9 }  { 5 6 }  7  { 4 8 } # subset of connected points

Find():
	are two objects in the same set?

Union():
	merge sets containing 2 points
	ie add a connection between 2 points
	
	Each union reduce by 1 the number of connected components


https://leetcode.com/problems/redundant-connection-ii/discuss/178903/Python-fast-Two-way-solution/189877
"""



def make_set(x, sets)
	if x not in sets:
		sets["x"]
   if x is not already present:
     add x to the disjoint-set tree
     x.parent := x
     x.rank   := 0
     x.size   := 1