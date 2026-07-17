class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_stot = {}
        map_ttos = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            
            if char_s in map_stot:
                if map_stot[char_s] != char_t:
                    return False
            else:
                map_stot[char_s] = char_t

            
            if char_t in map_ttos:
                if map_ttos[char_t] != char_s:
                    return False
            else:
                map_ttos[char_t] = char_s

        return True