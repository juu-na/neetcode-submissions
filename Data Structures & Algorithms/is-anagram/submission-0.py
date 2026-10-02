class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = sorted(list(s))
        t_char = sorted(list(t))

        if s_char == t_char:
            return True
        return False
