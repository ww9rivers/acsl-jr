'''PROBLEM Description:

	Given a positive integer (call it N), a position in that integer (call it P), and a
	transition integer (call it D). Transform N as follows:
	●	If the P-th digit of N from the right is from 0 to 4, add D to it. Replace
		the P-th digit by the units digit of the sum. Then, replace all digits to
		the right of the P-th digit by 0.
	●	If the P-th digit of N from the right is from 5 to 9, subtract D from it.
		Replace the P-th digit by the leftmost digit of the absolute value of the difference.
		Then, replace all digits to the right of the P-th  digit by 0.

Example 1:	N = 7145032, P = 2, D = 8. The 2nd digit from the right is 3; add 8 to it (3+8=11),
		and replace the 3 with 1 to get 7145012. Replace the digits to the right by 0s to get 7145010.
Example 2:	N = 1540670, P = 3, D = 54. The 3rd digit from the right is 6; the absolute value of
		6-54 is 48; replace with the 4 to get 1540470. Replace the digits to the right with 0s to get
		1540400.

INPUT:	There will be 5 sets of data. Each set contains 3 positive integers: N, P, and D. N will be
	less than 10 ; P and D will be valid inputs. No input will cause an output to have a leading digit 15
	of 0.
OUTPUT:	Print the transformed number. The printed number may not have any spaces between the digits.
SAMPLE INPUT: ( http://www.datafiles.acsl.org/2020/contest1/jr-sample-input.txt )
	124987	2 3
	540670	3 9
	7145042	2 8
	124987	2 523
	4386709	1 2
SAMPLE OUTPUT:
	1. 124950
	2. 540300
	3. 7145020
	4. 124950
	5. 4386707
'''

def transform(N, P, D):
	'''This will be shown as the doc for the transform() function.
	'''
	nx = list(str(N))	# list of digits in N
	np = int(nx[-P])	# P-th digit in N from the right
	if np >=0 and np <= 4:
		nx[-P] = str((np+D)%10)
	else:
		nx[-P] = list(str(abs(np-D)))[0]
	for i in range(-P+1, 0, 1):
		nx[i] = '0'
	print(''.join(nx))

transform(7145032, 2, 8)
transform(1540670, 3, 54)

data = [
	[124987,	2,	3],
	[540670,	3,	9],
	[7145042,	2,	8],
	[124987,	2,	523],
	[4386709,	1,	2],

	[4318762,	4,	3],
	[72431685,	1,	7],
	[123456789,	7,	8],
	[9876543210,	10,	25],
	[314159265358,	8,	428]
]

for xd in data:
	transform(*xd)