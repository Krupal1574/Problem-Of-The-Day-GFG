class Solution:
    def power(self, b: float, e: int) -> float:
        result = 1.0
        exp = abs(e)
        while exp > 0:
            if exp % 2 == 1:
                result *= b
            b *= b
            exp //= 2
        return result if e >= 0 else 1.0 / result