class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        s = ""
        word1_len = len(word1)
        word2_len = len(word2)
        while word1_len >= i+1 or word2_len >= i+1:
            if word1_len >= i + 1:
                s = s + word1[i]
            if word2_len >= i + 1:
                s = s + word2[i]
            i = i + 1
        return s