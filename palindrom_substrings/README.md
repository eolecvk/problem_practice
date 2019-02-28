
# Palindrom substring problem

## Description

You have been provided a file with a list of strings. Each string is on a new line.
The size of the file could be anywhere between 0MB - 1000MB.

Write a program/script to count and print lines which have the following pattern

Any 4 char sequence which has a pair of two different characters followed by the reverse of that pair
e.g xaax or raar. The string is not considered valid if the pattern above exist in square brackets.

For example:
```
rttr[mnop]qrst 			this is valid  	(rttr outside square brackets).
efgh[baab]ommo 			this is invalid (baab is within brackets, ommo outside brackets).
bbbb[qwer]ereq 			this is invalid (bbbb is invalid, since the middle two characters should be different.
irttrj[asdfgh]zxcvbn 	this is valid 	(rttr is outside square brackets).
```

## Algo and implementation

The file fits in memory so we can safely assume that each line fits in memory.

The program defines:

+ a sliding window as an char array of size 4

	+ the sliding window allows to quickly check if a given substring is a valid palindrom; ie

		- it is 4 chars long
		- last char is equal to first, second is equal to third

	+ a stack of containing palindroms and their respective depth (ie number of preceding open brackets).

		- an open bracket increment the depth counter for palindroms added to the stack
		- a closing bracket:

			- removes any palindrom with a depth matching the current number of open_brackets (ie palindrom is within brackets, at the level of the last bracket added)
			- decrement the depth counter for palindroms added to the stack


The program iterates over the line indices, effectively sliding the first index of the window along the line.  
A counter tracks the number of open brackets.  
The stack gets updated:

+ `pop()`: in case a palindrom with depth matching the previous number of open brackets is found. The palindrom is removed from the stack. This means that a palindrom is within brackets somewhere on the line so we can readily declare the line as invalid. 
+ `push()`: in case a palindrom is found at the current position of the sliding window.



## Complexity

This runtime complexity of this algorithm for a single line is linear in the length of the line because we need to iterate over each index and at each index do constant work to evaluate the palindrom, and possibly update the bracket counter and the stack.

The memory complexity of this algorithm for a sinle line is linear in the length if the line. In the worst case scenario, the stack will contain the entire line, stored as a stack of 4 character long palindroms.
