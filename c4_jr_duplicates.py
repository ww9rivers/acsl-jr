'''
PROBLEM: Consider a sorted array containing the letters COMPUTER:
C E M O P R T •••

When a letter is added, you insert the letter in the correct place in the array, moving the other letters. If the
letter is already in the array, insert it BEFORE the existing occurrence.
Continuing with the example above, let’s add the letters BAT. The shaded ([x]) cell is where the new letter is
positioned:
	1  2  3  4  5  6  7  8  9  ...
Add B: [B] C  E  M  O  P  R  T •••
Add A: [A] B  C  E  M  O  P  R  T •••
Add T:  A  B  C  E  M  O  P  R [T] T •••

INPUT: You’ll process 5 lines of data. Each line will start with a positive number, N, followed by a
space, and then a string, xxx. Into an empty array, insert each letter in the string, one at a time. Ignore non-letters and also, convert all lowercase letters into uppercase.

OUTPUT: For each input line, print how many different letters occupied the Nth element of the array
while the string was processed. For example, “2 Computer” has answer of 3: The different letters in
position 2 of the array were O, M, and finally E. The input line “2 COMPUTER Bat” has an answer of 5:
the different letters at position 5 were O, M, E, C, and B.

SAMPLE INPUT:		SAMPLE OUTPUT:
2 Computer		1. 3
2 COMPUTER bat		2. 5
3 COMPUTER		3. 2
4 ACSL is fun		4. 3
9 the xylophone		5. 4

TEST INPUT
3 python
3 computers
7 the quick brown fox
9 she sells sea shells by the sea shore
5 american computer science league

TEST OUTPUT
1. 4
2. 2
3. 6
4. 4
5. 5
'''
def process(input):
	N, xstr = input.split(' ', 1)
	letters = []
	lset = set()
	N = int(N)
	for xc in xstr:
		uc = xc.upper()
		if uc < 'A' or uc > 'Z': continue
		i = 0
		if len(letters) > 0:
			for i in range(len(letters)):
				if letters[i] >= uc:
					letters[(i+1):] = letters[i:]
					break
		if len(letters) == 0 or uc > letters[i]:
			letters.append(uc)
		else:
			letters[i] = uc
		if len(letters) >= N:
			lset.add(letters[N-1])
	# print(N, xstr, letters)
	print(len(lset))

process('2 Computer')
process('2 COMPUTER bat')
process('3 COMPUTER')
process('4 ACSL is fun')
process('9 the xylophone')
process('3 python')
process('3 computers')
process('7 the quick brown fox')
process('9 she sells sea shells by the sea shore')
process('5 american computer science league')
