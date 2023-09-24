class Solution:
    def romanToInt(self, s: str) -> int:
        rom2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman = list(s)
        num = 0
        for i in range(len(roman)):
            if i != len(roman) - 1 and rom2int[roman[i]] < rom2int[roman[i+1]]:
                num -= rom2int[roman[i]]

            else:
                num += rom2int[roman[i]]

        return num
