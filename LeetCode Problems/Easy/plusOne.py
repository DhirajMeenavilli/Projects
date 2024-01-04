digits = [1,2,3]
num = 0

for i in range(len(digits)):
    num += digits[i] * 10**(len(digits)-i-1)

num = list(str(num + 1))

for i in range(len(num)):
    num[i] = int(num[i])

print(num)