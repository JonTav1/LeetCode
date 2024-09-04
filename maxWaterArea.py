class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #it's gonna be lower height of two times distance between them
        left = 0
        right = len(heights) - 1
        amount_water = 0
        #two-pointer
        while left < right:
            height = min(heights[left], heights[right])

            if (height * (right-left)) > amount_water:
                amount_water = height * (right - left)
            #compare heights, whichever heights is greater, increment the other
            if heights[left] < heights[right] or heights[left] == heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1 
            

        
        return amount_water 

