class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split(" ")

        dictionary_set = set(dictionary)
        
        def find_root(word):
            for i in range(1, len(word) + 1):
                if word[:i] in dictionary_set:
                    return word[:i]
            return word

        result = []
        for word in words:
            root = find_root(word)
            result.append(root)

        new_sentence = " ".join(result)

        print(new_sentence)
        return new_sentence

