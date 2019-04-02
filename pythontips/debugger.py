"""
cf https://book.pythontips.com/en/latest/
"""

import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"


def test():
	j = 0
	for i in range(5):
		pdb.set_trace()
		j += 1

test()