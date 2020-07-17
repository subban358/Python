class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
    def permute(self, nums, startIndex, res):
        if startIndex == len(nums):
            temp = list(nums)
            res.append(temp)
            return
        for i in range(startIndex, len(nums)):
            self.swap(nums, startIndex, i)
            self.permute(nums, startIndex + 1, res)
            self.swap(nums, startIndex, i)
        
    def createPermutation(self, nums: List[int]) -> None:
        res = []
        self.permute(nums, 0, res)
        print(res)
                       
