# Given a non-negative number return the rounded down nearest interger.

# Structure: Positive number including 0 is given so we can say 0 -> 0, 1 -> 1, 2-> 1, 3 -> 1, 4 -> 2, 5 - 8 -> 2, 9 -> 3, 10 - 16 -> 4

val = 102

i = 2
running = True

if val == 0 or val == 1:
    print(1)

while running:
    if val >= i**2 and val < (i+1)**2:
        print(i)
        running = False
    
    i += 1

