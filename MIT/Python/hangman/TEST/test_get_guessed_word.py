#! /bin/python2.7

def get_guessed_word(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string, comprised of letters, underscores (_), and spaces that represents
	which letters in secret_word have been guessed so far.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	word = []
	string = ''
	for i in range(len(secret_word)):
		word.append('_ ')
	for i in range(len(secret_word)):
		for j in range(len(letters_guessed)):
			if secret_word[i] == letters_guessed[j]:
				word[i] = secret_word[i]
				break
	for i in range(len(word)):
		string += word[i]
	return string
secret_word = 'apple'
letters_guessed = ['e', 'a', 'l', 'p', 'r', 's']
print(get_guessed_word(secret_word, letters_guessed))
