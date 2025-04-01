class Solution:
    def longestUniqueSubstr(self, s):
        last_seen = [-1] * 128  
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            start = max(start, last_seen[ord(char)] + 1)
            last_seen[ord(char)] = end
            max_length = max(max_length, end - start + 1)

        return max_length