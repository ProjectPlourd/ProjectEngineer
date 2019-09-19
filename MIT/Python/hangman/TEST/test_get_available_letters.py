#! /bin/python2.7

def get_available_letters(letters_guessed):
	'''
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string (of letters), comprised of letters that represents which letters have not
	yet been guessed.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	string_lowercase = 'abcdefghijklmnopqrstuvwxyz'
	letter_list = ['']
	letters_not_guessed = ''

	for letter in range(len(string_lowercase)):
		letter_list.append(string_lowercase[letter])
	for i in range(len(letter_list)):
		for j in range(len(letters_guessed)):
			if letter_list[i] == letters_guessed[j]:
				letter_list[i] = ''

	for i in range(len(letter_list)):
		letters_not_guessed += letter_list[i]
	return letters_not_guessed


letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print get_available_letters(letters_guessed)

