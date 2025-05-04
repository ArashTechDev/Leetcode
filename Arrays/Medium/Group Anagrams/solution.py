class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            wordDigits = [0] * 26  
            for char in word:
                 # we start off with a list of 26 zeroes and we'll update a zero according to each alphabet
                charDigit = ord(char) - ord('a')
                wordDigits[charDigit] += 1          # we increase that alphabet occurence by 1 in the wordDigits list.
            # we now need to group similar wordDigits
            key = tuple(wordDigits)     # create tuple of wordDigits integers - so that unique key(hashable) are added to hashMap
            if key not in res:          
                res[key] = []           
            res[key].append(word)       # add the key to hashMap, set value to word - so that anagrams start grouping together
        return list(res.values())       # convert the dict view object to a list as our return type should be a list


