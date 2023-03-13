class AnagramChecker():
    def __init__(self):
        with open('word_list.txt') as f:
            self.local_list = []
            for line in f:
                line = line.strip()
                self.local_list.append(line)
            
    def is_valid_word(self, word):
        ''' should check if the given word (ie. the word of the user) is a valid word.'''
        for i in self.local_list:
            if i == word:
                return True
        else:
            return False

    def get_anagrams(self, input):
        '''should find all anagrams for the given word. (eg. if word of the user is 'meat', the function should return a list containing [“mate”, “tame”, “team”].)'''
        result_list = []
        for word_of_dict in self.local_list:
            if self.is_anagram(input, word_of_dict):
                result_list.append(word_of_dict)
        return result_list
    
    def is_anagram(self, word1, word2):
        '''will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not'''
        if word1 == word2:
            return False
        return sorted(word1) == sorted(word2)
    