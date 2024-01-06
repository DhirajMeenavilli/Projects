s = "wwekw"
arr = list(s)
chars = []
l = 0
r = 1
maxLen = 0

if len(arr) == 0:
    print(0)
    r = len(arr)

chars.append(arr[0])

while r < len(arr):

    if arr[r] in chars:
        if maxLen < len(chars):
            maxLen = len(chars)
        l = l + 1
        r = l + 1
        chars = []
        chars.append(arr[l])
    
    if r < len(arr):
        if arr[r] not in chars:
            chars.append(arr[r])
    
    else:
        print(maxLen)
        break
        
    r+=1

if maxLen < len(chars):
    maxLen = len(chars)

print(maxLen)