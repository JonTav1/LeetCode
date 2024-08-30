class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        max_candies = max(candies)
        bool_list = []
        for kid_candies in candies:
            if kid_candies + extraCandies >= max_candies:
                    bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list

        