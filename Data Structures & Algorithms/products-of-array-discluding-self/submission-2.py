class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1

        # Product of elements to the left
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Product of elements to the right
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

                    
        