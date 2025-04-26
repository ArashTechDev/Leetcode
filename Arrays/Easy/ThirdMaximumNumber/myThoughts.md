My Thoughts:
The solution i did has O(nlogn) time complexity. I will be updating this solution and try to get an o(n) solution.

This problem was easy to solve. Basically, I sorted the list using python's in-built library. I then used a for loop starting from the last index (where max num would be). And i started putting the values in a hashmap (for unique keys/value) and started a counter and waited until 3 key/value pairs were inserted (ThirdMaxNumber), and then returned the value at that index (nums[i]) OR the code would then return the index (nums[len(nums) - 1)

            
            

        
        
