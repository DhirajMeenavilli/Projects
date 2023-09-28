"""
Title: Broken Antennas Problem
Date: August 8, 2023
Author: Dhiraj Meenavilli
"""

import random

start = int(input("From what number of antenas would you like to start?"))
stop = int(input("At what number of antenas would you like to stop?"))


trials = 100000

avgCounts = []

while start != stop+1:
    endOfTrialcounts = []
    k = 2

    while k != (start // 2 + 1):
        print(start, k)
        for i in range(10): #So that there are 10 trials on each n choose k so that it can be averaged to find a realtively stable value for the amount of times that the communications system is gonna be out.

            antenas = start #int(input("How many antennas are there?"))
            bronkenAntenas = k #int(input("How many broken antennas are there?"))
            unbrokenAntenas = antenas - bronkenAntenas

            slots = [1] * bronkenAntenas + [0] * unbrokenAntenas

            count = 0

            # print("first",slots)

            def twoBrokenAntena(slots): #First and dumbest attempt but it is effective even though it is brute force a bit.
                for i in range(len(slots) - 1):
                    if slots[i] == 1 and slots[i + 1] == 1:
                        return True
                return False

            for i in range(trials):
                random.shuffle(slots)
                
                # print(trials,slots)

                #if slots == [1,1,0,0] or slots == [0,1,1,0] or slots == [0,0,1,1]: #If I can jsut change this so that I can see generally instead of just for the special case of 4 I think this counts as a proof of a sort
                    # print("hit")
                if twoBrokenAntena(slots):
                    count += 1

            # print(start, k, count/trials)

            trialAverage = count/trials

            endOfTrialcounts.append(trialAverage)

            # I was thinking about how to mathematically prove it, but what if instead I could graph out the map for the various n's and k's and get a machin to learn that function
        
        k += 1
        avgCounts.append(round(sum(endOfTrialcounts)/len(endOfTrialcounts),2))
        endOfTrialcounts = []

    start += 1

print(avgCounts) # So I effectively have all the averages, now I just need to plot this graphically on a 3d plane of n, k, probability of destroyed communications system