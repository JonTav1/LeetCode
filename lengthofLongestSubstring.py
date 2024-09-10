class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_string = 0
        sub_string = ""
        for i in range(len(s)):
            if s[i] not in sub_string:
                sub_string += s[i]
                print(sub_string)
            else:#take the characters from the last substring that aren't the repeated character
            #that we can use for the next sub_string
                sub_string = sub_string[sub_string.index(s[i])+1:] + s[i]
            if len(sub_string) > max_sub_string:
                max_sub_string = len(sub_string)
        return max_sub_string   
