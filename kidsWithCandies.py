class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # return the largest item/kid
        # iterate over kids with candies
        # if the sum of current candies + extra candies is larger than the max ammount of candies
        # the kid has the most 
        # else the kid doesn't have the most
        
        # Space Complexity = O(n) 
        # Time Complexity =  O(n)

        max_candy_amount = max(candies)
        for index in range(len(candies)):
            if candies[index] + extraCandies >= max_candy_amount:
                yield True
            else:
                yield False