class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_1 = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums_1:
                count = 1
                
                while (num + count) in nums_1:
                    count += 1
                    
                longest = max(longest,count)
        return longest
        