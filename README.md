# Boogle Solver

The goal of the game of Boggle consists in finding all the words that can be made by chaining adjacent letters in a `n x m` grid.
Adjacent letters are letters that are located in the same row or in the same column.
Each position on the grid can only be visited at most once per word.

## Data structure and algorithm**

**Prefix and word lookup**

In order to efficiently check the existence  of prefix and words, I implement a Trie (ie _prefix tree_) data structure and populate it with a reference vocabulary (see attached file).


**Word search**

The algorithm iterates over the `n x m` positions of the Boggle grid.
At each position, a Depth First Search is performed such that it searches for all the prefixes that can be made from paths of adjacent characters starting at the reference position. The DFS is implemented such that positions cannot be visited twice per search.

The DFS stop condition is based on whether the current chain of characters formed (prefix) exists in the reference prefix tree.
If a prefix formed exists in the tree and corresponds to a word according to the Trie, it is added to the output list of words.

