'''
PROBLEM: Easy as ABC is a puzzle game by Wei-Hwa Huang. In the puzzle the letters A, B and C
are placed in the grid so that each letter appears just once in each row and column. In addition some
letters will be placed in the puzzle at the start of the game. The game is played on a 3 x 3 grid.
	1 2 3		A _ C		A B C
	4 5 6		_ _ _		B C A
	7 8 9		_ A _		C A B

INPUT: There will be 5 lines of input. Each line will contain the number of letters in the grid at the start
of the game followed by their location (see the left grid) and the letter at that location. The data for
middle grid is Sample Data #1; the solution for data is at the right.

OUTPUT: For each input line print the resulting grid with the letters in the correct positions. The letters
must be printed on one line in grid number order 1 – 9.

SAMPLE INPUT:			SAMPLE OUTPUT:
1. 3, 1, A, 3, C, 8, A		1. ABCBCACAB
2. 3, 1, A, 6, C, 8, B		2. ACBBACCBA
3. 3, 1, B, 6, B, 9, C		3. BCACABABC
4. 2, 1, C, 5, B		4. CABABCBCA
5. 2, 3, B, 7, A		5. CABBCAABC

TEST INPUT			TEST OUTPUT
1. 4, 1, A, 2, B, 8, A. 9, B	1. ABCBCACAB
2. 3, 1, A, 2, B, 9, A		2. ABCCABBCA
3. 3, 3, C, 6, B, 7, C		3. BACACBCBA
4. 2, 7, A, 6, C		4. CBABACACB
5. 2, 1, C, 6, A		5. CABBCAABC
'''
ABC = set({'A', 'B', 'C'})
GRIDZ = 3*3
def process(abc):
	grid = [0]*GRIDZ
	# Initialize the grid
	count = GRIDZ - abc[0]
	for i in range(abc[0]):
		grid[abc[2*i+1]-1] = abc[2*i+2]
	# Fill cross points:
	while count > 0:
		for i in range(GRIDZ):
			row = 3 if i < 3 else 6 if i < 6 else 9
			if grid[i] == 0:
				r1 = i+1
				r2 = i+2
				if r1 >= row: r1 -= 3
				if r2 >= row: r2 -= 3
				c1 = i+3
				c2 = i+6
				if c1 >= GRIDZ: c1 -= GRIDZ
				if c2 >= GRIDZ: c2 -= GRIDZ
				cell = ABC - set({grid[r1], grid[r2], grid[c1], grid[c2]})
				if len(cell) == 1:
					grid[i] = list(cell)[0]
					count -= 1
	print(''.join(grid))

process([3, 1, 'A', 3, 'C', 8, 'A'])		# 1. ABCBCACAB
process([3, 1, 'A', 6, 'C', 8, 'B'])		# 2. ACBBACCBA
process([3, 1, 'B', 6, 'B', 9, 'C'])		# 3. BCACABABC
process([2, 1, 'C', 5, 'B'])			# 4. CABABCBCA
process([2, 3, 'B', 7, 'A'])			# 5. CABBCAABC
print()
process([4, 1, 'A', 2, 'B', 8, 'A', 9, 'B'])	# 1. ABCBCACAB
process([3, 1, 'A', 2, 'B', 9, 'A'])		# 2. ABCCABBCA
process([3, 3, 'C', 6, 'B', 7, 'C'])		# 3. BACACBCBA
process([2, 7, 'A', 6, 'C'])			# 4. CBABACACB
process([2, 1, 'C', 6, 'A'])			# 5. CABBCAABC
