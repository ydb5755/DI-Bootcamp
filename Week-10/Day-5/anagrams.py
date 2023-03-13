# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.

from anagram_checker import AnagramChecker
def anagram_checker_func():
    checker = AnagramChecker()
    while True:
        word = input('Please enter one word in capital letters or "exit" to exit the program:  ').strip()
        print(word)
        if word == 'exit':
            print('No problem, see you later')
            break
        if word.find(' ') != -1:
            print('Please enter ONLY ONE WORD')
            continue
        if word.upper() != word:
            print('Please enter the word in UPPERCASE')
            continue
        if checker.is_valid_word == False:
            print('You entered your word correctly, its just not a real word, enter a real word this time please')
            continue
        list_of_anagrams = checker.get_anagrams(word)
        string_of_anagrams = ''
        for word_of_anagram_list in list_of_anagrams:
            string_of_anagrams += word_of_anagram_list + ' '
        print(f'YOUR WORD : "{word}"\nThis is a valid English word\nAnagrams for your word are: {string_of_anagrams}')
        break

anagram_checker_func()

