class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1, -1):
            digits[i]+=1
            if digits[i]%10 > 0:
                return digits
            digits[i]%=10
        digits[0] = 1
        digits.append(0)
        return digits