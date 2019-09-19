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
# string get_available_letters
# string get_guessed_word
# boolean is_word_guessed
def hangman(secret_word):
	'''
	secret_word: string, the secret word to guess.

	Starts up an interactive game of Hangman.

	* At the start of the game, let the user know how many 
	letters the secret_word contains and how many guesses s/he starts with.

	* The user should start with 6 guesses

	* Before each round, you should display to the user how many guesses
	s/he has left and the letters that the user has not yet guessed.

	* Ask the user to supply one guess per round. Remember to make
	sure that the user puts in a letter!

	* The user should receive feedback immediately after each guess 
	about whether their guess appears in the computer's word.

	* After each guess, you should display to the user the 
	partially guessed word so far.

	Follows the other limitations detailed in the problem write-up.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	letters_guessed = []
	guesses_left = 6

	print ("Loading word list from file...")
	print ("55900 words loaded.")
	print ("Welcome to the game Hangman!")
	print ("I am thinking of a secret word that has "+ str(len(secret_word))+ " letters in it.")

	while (guesses_left > 0) and not (is_word_guessed(secret_word, letters_guessed)):
		print ("You have "+ str(guesses_left)+ " guess(es) left")
		print ("Available letters: "+ get_available_letters(letters_guessed))
		letters_guessed.append(input())
		guesses_left -= 1
		if is_word_guessed(secret_word, letters_guessed):
			print ("Left Hip Right Hip Hurray you guessed it!")
			break
	if guesses_left == 0:
		print("Aww I got you this time.")
		print("You guessed", get_guessed_word(secret_word, letters_guessed))
	print("The secret word was", secret_word)


hangman('hello')

