# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
from collections import Counter
class Text():
    def __init__(self, input_str):
        self.input_str = input_str
        self.split_string = input_str.split(' ')

    def return_frequency_of_word_in_text(self, word):
        freq  = self.split_string.count(word)
        if freq == 0:
            return None
        else:
            return f"The word '{word}' appears in this text {freq} times"

    def return_the_most_common_word_in_the_text(self):
        freq = Counter(self.split_string)
        most = 0
        for word in freq:
            if freq[word] > most:
                most = freq[word]
                largest_word = word
        return largest_word

    def return_a_list_of_all_the_unique_words_in_the_text(self):
        freq = Counter(self.split_string)
        unique = []
        for word in freq:
            if freq[word] == 1:
                unique.append(word)
        return unique
    
    @classmethod
    def from_file(cls, file):
        with open(file) as f:
            return cls(f.read())

test = Text.from_file('the_stranger.txt')
print(test.return_frequency_of_word_in_text('you'))
# test1 = Text('a method to return the frequency of a word in the text')
# print(test1.return_a_list_of_all_the_unique_words_in_the_text())
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.



# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

