# your code goes here!
class Anagram :
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))
    
    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            sorted_candidate = ''.join(sorted(candidate))
            if sorted_candidate == self.sorted_word:
                matches.append(candidate)
        return matches