
'''
1- A string of arbitrary length
2- We are trying to find the longest chain without repeated chars

can be a tree where nodes know their parents
'''


class Solution:
    def quadratic(self, s: str) -> str:
        longest = ""
        current = ""
        for char in s:
            if char not in current:
                current += char
                if len(current) > len(longest):
                    longest = current
            else:
                current = ""
        return longest
    
    def usingSets(self, s: str) -> str:
        longest = ""
        current = ""
        currentSet = set()
        for char in s:
            if char not in currentSet:
                current += char
                currentSet.add(char)
                if len(currentSet) > len(longest):
                    longest = current
            else:
                currentSet = set()
                current = ""
        return longest
