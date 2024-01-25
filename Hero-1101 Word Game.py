# Problem 1
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    """
    for every letter in secret_word
        if the letter is not in letters_guessed
            stop looking and return false
    return true
    """
 
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
       
 
# Testcases
print(is_word_guessed('carrot', ['c', 'o', 'i', 'n', 'p', 'r', 's']))
print(is_word_guessed('blueberry', ['s', 'z', 'q', 'b', 'l', 'u', 'e', 'b', 'e', 'r', 'r', 'y', ]))
print(is_word_guessed('coconut', []))
 
# # Problem 2
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    output_string = ""
    for letter in secret_word:
        if letter in letters_guessed:
            output_string += letter + " "
        else:
            output_string += "_ "
    return output_string
 
print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print(get_guessed_word('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
print(get_guessed_word ('banana', []))
 
# # Problem 3
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''  
    import string
    alphabet = list(string.ascii_lowercase)
 
    for letter in alphabet:
        if letter in letters_guessed:
            alphabet.remove(letter)
 
    return ' '.join(alphabet)
   
print(get_available_letters('apple'))
print(get_available_letters(''))
