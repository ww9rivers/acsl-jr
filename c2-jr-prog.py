'''
PROBLEM: Given a sentence (up to 1024 characters long), output the following:
1) The number of different letters. This will be a number from 1 to 26, inclusive.
2) The number of vowels. Vowels are the letters a, e, i, o, and u.
3) The number of uppercase letters.
4) The number of times that the most frequent letter appears. There is no distinction between lowercase and uppercase letters.
5) The longest word in the sentence. If there is a tie, print the one that appears first when sorting these words alphabetically without regard to lowercase and uppercase.

INPUT: One line of data, containing a sentence, up to 1024 characters long.
OUTPUT: Print the five statistics specified above in that order.
SAMPLE INPUT http://www.datafiles.acsl.org/2019/contest2/jr-sample-input.txt
The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog.
SAMPLE OUTPUT
1. 25
2. 19
3. 3
4. 6
5. Roxanne
'''
import re
Vowels = 'AEIOU'

def reverse_word_comp(x, y):
	'''Compare two words, x and y, by length and alphabetical order.'''
	diff = len(y)-len(x)
	if diff == 0:
		diff = 1 if x > y else -1 if x < y else 0
	return diff

def cmp_to_key(mycmp):
	'''Convert a cmp= function into a key= function'''
	class K:
		def __init__(self, obj, *args):
			self.obj = obj
		def __lt__(self, other):
			return mycmp(self.obj, other.obj) < 0
		def __gt__(self, other):
			return mycmp(self.obj, other.obj) > 0
		def __eq__(self, other):
			return mycmp(self.obj, other.obj) == 0
		def __le__(self, other):
			return mycmp(self.obj, other.obj) <= 0
		def __ge__(self, other):
			return mycmp(self.obj, other.obj) >= 0
		def __ne__(self, other):
			return mycmp(self.obj, other.obj) != 0
	return K

def process(sentence):
	print('')
	print(sentence)
	letter_set = set()
	letter_freq = {}
	count_vowel = 0
	count_upper = 0
	for xc in sentence:
		# Count if a letter:
		uc = xc.upper()
		if uc >= 'A' and uc <= 'Z':
			letter_set.add(uc)
			# Count if vowel:
			if uc in Vowels:
				count_vowel += 1
			# Count uppercase letters:
			if xc >= 'A' and xc <= 'Z':
				count_upper += 1
			# Build letter frequency:
			if uc in letter_freq:
				letter_freq[uc] += 1
			else:
				letter_freq[uc] = 1
	print(len(letter_set))
	print(count_vowel)
	print(count_upper)
	top_freq = 0
	for uc, freq in letter_freq.items():
		if freq > top_freq:
			top_freq = freq
	print(top_freq)

	# Break the sentence into words:
	words = sorted(re.split('[^\w]+', sentence), key = cmp_to_key(reverse_word_comp))
	print(words[0])

process('The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog.')
process('This is a special sentence, one with two non-word strings: aaaaaaaa zzzzzzzz.')