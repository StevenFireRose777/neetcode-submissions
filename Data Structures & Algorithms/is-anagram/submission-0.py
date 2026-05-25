class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        """
        1. What is NOT an anagram
            a. String lengths are NOT equal
            b. One or more chars in either string are different
        2. What is an anagram
            a. Every character from each string match each other

        3. If the strings have th same lengths, sort the strings by alphabetical order
            a. for n in string:
                
        """

        if len(s) != len(t):
            return False
        
        sorted_chars = sorted(s)
        s = "".join(sorted_chars)

        sorted_chars = sorted(t)
        t = "".join(sorted_chars)


        if s == t:
            return True
        else:
            return False

    


