import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_origin = nums.copy()
        self.nums = nums
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.nums_origin.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
