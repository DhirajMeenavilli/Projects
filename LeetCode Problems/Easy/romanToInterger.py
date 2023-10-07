class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000,500,100,50,10,5,1]
        romans = ['M','D','C','L','X','V','I']
        amounts = [0,0,0,0,0,0,0]
        roman = ''

        for i in range(len(vals)):
            amounts[i] = num // vals[i]
            num -= vals[i]*amounts[i]

            roman += romans[i] * amounts[i]
            
            if num // 900 == 1 and num % 900 <= 99:
                roman += 'CM'
                num -= 900

            if num // 400 == 1 and num % 400 <= 99:
                roman += 'CD'
                num -= 400

            if num // 90 == 1 and num % 90 <= 9:
                roman += 'XC'
                num -= 90
            
            if num // 40 == 1 and num % 40 <= 9:
                roman += 'XL'
                num -= 40

            if num // 9 == 1 and num % 9 <= 0:
                roman += 'IX'
                num -= 9

            if num // 4 == 1 and num % 4 <= 0:
                roman += 'IV'
                num -= 4

        return roman