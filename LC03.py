class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, begin, last_pos = 0, 0, {}
        #invariant there are no repeating charst between begin and i - 1
        for i, c in enumerate(s):
            # Notice that it has to be <= not < here, since we need to make sure when i points to a seen char and that seen char is not at the 'begin' pos
            if c in last_pos and begin <= last_pos[c]:
                begin = last_pos[c] + 1
            max_len = max(max_len, i - begin + 1)
            last_pos[c] = i
        return max_len
