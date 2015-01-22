# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
def hangman():
    wordlist = load_words()
    word = choose_word(wordlist)
    length = len(word)
    import string
    alphabet = string.lowercase
    alphabetlist = list(alphabet)
    print 'The word I am thinking of is', length, 'letters long'
    chance = 8
    blankwordlist = []
    for blanks in range(0, length):
        blankwordlist = blankwordlist + ['_ ']
    blankword = ''.join(blankwordlist)
    print blankword
    while chance > 0:
        print 'You have', chance, 'guesses left'
        print 'Available letters:', alphabet
        guess = raw_input('Please guess a letter: ').lower()
        if len(guess) ==1:
            letterremoval = alphabet.find(guess)
            del alphabetlist[letterremoval]
            alphabet = ''.join(alphabetlist)
            lettercount = word.count(guess)
            check = word.find(guess)
            if check == -1:
                chance -=1
                print blankword
            else:
                for occurance in range(0, lettercount):
                    if occurance > 0:
                        checknew = word.find(guess, (check + 1))
                        check = checknew
                        blankwordlist[check] = guess
                    else:
                        blankwordlist[check] = guess
                blankword = ''.join(blankwordlist)
                print blankword
        else:
            print 'Please guess only a single letter'
        if blankword == word:
            break
    if blankword == word:
        print 'You win!'
    if chance == 0:
        print 'you lose'
        print 'The word was:', word
            
hangman()

