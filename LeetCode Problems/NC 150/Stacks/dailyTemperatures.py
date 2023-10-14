def dailyTemperatures(self, temperatures: [int]) -> [int]: # Brote Force is O(N^2) having to search every value against every value. I can also think of way to do it with O(N^2) memory but that'd be tricky and possibly too much storage.
    answer = []
    interim = []
    
    curr = temperatures[0]
    
    for i in range(len(temperatures)):

        interim.append(temperatures[i])

        if temperatures[i] > curr:
            print(interim)
            while len(interim) > 1:
                answer.append(len(interim)-1)
                interim.remove(interim[0])

            curr = interim[0]

    while len(answer) < len(temperatures):
        answer.append(0)
    
    return answer