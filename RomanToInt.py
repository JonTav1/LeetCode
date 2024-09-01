class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        numerals = {"I": 1, "IV" : 4, "IX": 9, "V" : 5, "X": 10, "XL": 40, "XC" : 90, "L": 50, "C": 100, "CD" : 400, "CM" : 900, "D" : 500, "M" : 1000}
        total = 0
        while i < len(s):

            if i+1 < len(s) and s[i] + s[i+1] in numerals:
                total = total + numerals.get(s[i] + s[i+1])
                i = i+2
            else:
                total = numerals.get(s[i]) + total
                i = i+1
        return total


            


        