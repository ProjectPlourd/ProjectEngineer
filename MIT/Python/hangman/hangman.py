#! /bin/python2.7
import random
import string

# Hangman Game
# -----------------------------------

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

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
	guess = ' '
	warnings = 3
	already_guessed = False

	print ("Loading word list from file...")
	print ("55900 words loaded.")
	print ("Welcome to the game Hangman!")
	print ("I am thinking of a secret word that has "+ str(len(secret_word))+ " letters in it.")
	while (guesses_left > 0) and not (is_word_guessed(secret_word, letters_guessed)):
		print "You have", warnings, "warnings left" 
		print "You have", guesses_left, "guess(es) left"
		print "Available letters: "+ get_available_letters(letters_guessed)
		guess = raw_input("Please guess a letter: ")
		for i in range(len(letters_guessed)):
			if guess == letters_guessed[i]:
				already_guessed = True	
		if str.isalpha(guess) and already_guessed != True:
			letters_guessed.append(str.lower(guess))
			guesses_left -= 1
		elif warnings == 0:
			guesses_left -= 1
		elif already_guessed:
			warnings -= 1
		else:
			warnings -= 1	
		if is_word_guessed(secret_word, letters_guessed):
			print "Left Hip Right Hip Hurray you guessed it!"
			break
	if guesses_left == 0:
		print "Aww I got you this time."
		print "You guessed", get_guessed_word(secret_word, letters_guessed)
	print "The secret word was", secret_word

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)


