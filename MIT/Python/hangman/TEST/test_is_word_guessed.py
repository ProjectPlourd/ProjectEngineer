#! /bin/python2.7
import sys

def is_word_guessed(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing; assumes all letters are
	lowercase
	letters_guessed: list (of letters), which letters have been guessed so far;
	assumes that all letters are lowercase
	returns: boolean, True if all the letters of secret_word are in letters_guessed;
	False otherwise
	'''
	#secret_word = 'apple'
	#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	count = 0
	for i in range(len(secret_word)):
		for j in range(len(letters_guessed)):
			if secret_word[i] == letters_guessed[j]:
				count += 1
				break
	if count == len(secret_word):
		return True
	else:
		return False
secret_word = 'apple'
letters_guessed = ['e', 'a', 'l', 'p', 'r', 's']
print(is_word_guessed(secret_word, letters_guessed))
