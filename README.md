# ACSL Junior Programming Problems

This folder contains the [ACSL](https://www.acsl.org/)
[Junior league](https://www.acsl.org/get-started/study-materials) programming problems.

## c1_jr_transform.py

2019-2020 ACSL [Junior Division - Number Transformation](http://www.datafiles.acsl.org/samples/contest1/C_1_JR_Transform.pdf).

In the ```process(N, P, D)``` function, the number _N_ is transformed into a string then broken up into a
list of digits for easier manipulation and replacement of digits by position.

## c2-jr-prog.py

2018-2019 ACSL [Junior Division - String Stats](http://www.datafiles.acsl.org/samples/contest2/c2-jr-prog.pdf).

The ```process(sentence)``` function in this one uses regular expression to split the sentence into a list of words.
Also, the Python3 sort function uses a _key_ function that takes an item then returns a value for comparison. These
two subjects may be advanced for ACSL junior division students.

## c3_jr_abc.py

2015-2016 ACSL [Junior Division Programming Problem: ACSL ABC](http://www.datafiles.acsl.org/samples/contest3/abc_3_jr.pdf).

The algorithm is to repeatedly loop through all empty cells in the grid and calculate the set of letters in the same row and
the same column of that cell. If only one letter is missing from that set, fill the current empty cell with that letter.
Repeat until all cells are filled.

For example:

| &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- |
| &nbsp; | &nbsp; | *C* |
| &nbsp; |   *A*  | &nbsp; |

In the first iteration, cell 5 and cell 9 would be filled with ```B```;

In the second iteration, all cells except for cell 1 would be filled;

In the third iteration, cell 1 would be filled and the grid is complete.

## c4_jr_duplicates.py

2017-2018 ACSL [Junior Division Programming Problem: Duplicates](http://www.datafiles.acsl.org/samples/contest4/c_4_duplicates_jr.pdf).

In this program, again, a set variable ```lset``` is used to compute the number of different (unique) letters.

## Author

* Wei Wang <ww@9rivers.com>