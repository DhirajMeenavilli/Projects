preferncesOfWhoToReccomendTo = ['carrot','cabbage','fish','meat'] # We can remove the fact that it's rabbit who is making these reccomendations.

ratings = [['cabbage','carrot','fish','meat'],['fish','meat','carrot','cabbage'],['meat','fish','cabbage','carrot']] # In the same way, we can forget that it's trurtle, cat and dog doing these ratings just their index is fine.

raters = ['turtle', 'cat', 'dog'] # Using this we can check at the end of the algorithim that the raters names are being disp[layed even if they're nothing more than an index in the program.


conversion = {'carrot': 1, 'cabbage': 2, 'fish': 3, 'meat': 4}

convertedRatings = []
for i in range(len(ratings)):
    convertedRatings.append([])
    for j in range(len(ratings[i])):
        convertedRatings[i].append(conversion[ratings[i][j]])

counts = {}

for i in range(len(convertedRatings)):
    invCount = 0
    for j in range(len(convertedRatings[i])):
        for k in range(j+1, len(convertedRatings[i])):
            if convertedRatings[i][j] > convertedRatings[i][k]:
                invCount += 1
    counts[raters[i]] = invCount

sortedCounts = dict(sorted(counts.items(), key=lambda key_val: key_val[1]))

output = ','.join(list(sortedCounts.keys()))
print(output)




