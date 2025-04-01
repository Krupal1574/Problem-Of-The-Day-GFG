3
from itertools import permutations

class Solution:
    def findPermutation(self, s):
        return sorted(set(["".join(p) for p in permutations(s)]))  # Unique permutations