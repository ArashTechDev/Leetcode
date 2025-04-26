My Thoughts:
The solution i did has O(nlogn) time complexity. I will be updating this solution and try to get an o(n) solution.

This problem was easy to solve. Basically, I sorted the list using python's in-built library. I then used a for loop starting from the last index (where max num would be). And i started putting the values in a hashmap (for unique keys/value) and started a counter and waited until 3 key/value pairs were inserted (ThirdMaxNumber), and then returned the value at that index (nums[i]) OR the code would then return the index (nums[len(nums) - 1)


###PROBLEM
414. Third Maximum Number
Solved
Easy
Topics
Companies

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

 
Follow up: Can you find an O(n) solution?


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        hashMap = {}
        index = 0
        for i in range(len(sorted_nums) - 1,-1, -1):
            if sorted_nums[i] not in hashMap.values():
                hashMap[index] = sorted_nums[i]
                if index == 2:
                    return hashMap[2]
                index
        return hashMap[0]

            
            

        
        
