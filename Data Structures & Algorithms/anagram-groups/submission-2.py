class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total_anagrams = []
        my_dict = {} # key = sorted word, value = a list of valid strs
        for word in strs:
            # print(word)
            s_word = "".join(sorted(word))
            if s_word not in my_dict:
                my_dict[s_word] = [word]
            else:
                my_dict[s_word].append(word) 
        # print(my_dict)
        for value in my_dict.values():
            total_anagrams.append(value)
        return total_anagrams
        