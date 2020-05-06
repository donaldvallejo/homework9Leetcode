class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # instantiate the starting point 
        i = 0
        # iterate over element 
        # if the target number is not the same as the value
        # compare the first and second element and increment the first one by + 1 
        # else return

        # Space Complexity = O(n)
        # Time Complexity = O(n)
        for j, n in enumerate(nums):
            if n != val:
                nums[i] = nums[j]
                i += 1
        
        return i