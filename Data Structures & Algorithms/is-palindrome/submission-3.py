class Solution:

    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        # Removing non-alphanumeric chars + whitespace
        for char in s:
            if not char.isalnum():
                continue
            else:
                s2 += char.lower()
        # print(s_2)
        # reversed_s2 = s2
        # print(f"This is s_2: {s_2}")
        right = len(s2) - 1    
        left = 0
        # r_s2 = ""
        l_s2 = list(s2)
        # print(l_s2)
        while left <= right:
            temp = l_s2[left]
            l_s2[left] = l_s2[right]
            l_s2[right] = temp
            left += 1
            right -= 1
        # print(l_s2)

        # Can compare lists apprently
        if l_s2 == list(s2):
            return True

        
        return False
        