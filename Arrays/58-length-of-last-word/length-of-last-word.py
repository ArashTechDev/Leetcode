class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        space = ' '
        counter = 0
        if s[i] is space:
            while s[i] is space and i >=0:
                i-=1
            while s[i] is not space and i >=0:
                counter += 1
                i-=1
            return counter
        else:
            while s[i] is not space and i >=0:
                counter +=1
                i-=1
            return counter
            
       
       
