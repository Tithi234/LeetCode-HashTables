from collections import defaultdict

class  Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create a dictionaryto map sorted word -> list of anagrams
        anagrams = defaultdict(list)

        for word in strs:
            # Sort the word and use it as key
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)

        # Return all the grouped anagrams
        return list(anagrams.values())
    
