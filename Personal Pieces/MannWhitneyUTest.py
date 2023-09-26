first_sample_observations = [0,1,1,2,3,5,8,12,18,22,26,39,42,44,47,48,49]
second_sample_observations = [0,0,0,1,2,3,4,9,13,20,28,29,30,33] 

new_array = first_sample_observations + second_sample_observations

new_array.sort()
copy = new_array.copy()
# print(new_array.count(0))
repeats = []
ranks = []
# print(sum(range(3,7)))

for i in range(len(new_array)):

    if new_array[i] in repeats:
        new_array[i] = 'Skip'

    if new_array[i] != 'Skip':
        if new_array.count(new_array[i]) > 1:
            first = sum(range(i+1, i + new_array.count(new_array[i])+1))
            second = new_array.count(new_array[i]) 
            val = first / second 
            repeats.append(new_array[i])
        else:
            val = i + 1
    
        ranks.append(val)

    else:
        ranks.append(val)

first_copy = first_sample_observations.copy()
second_copy = second_sample_observations.copy()

for i in range(len(copy)):
    if copy[i] in first_sample_observations:
        first_copy[first_copy.index(copy[i])] = ranks[i]
        first_sample_observations[first_sample_observations.index(copy[i])] = 'Done'
        
    elif copy[i] in second_sample_observations:
        second_copy[second_copy.index(copy[i])] = ranks[i]
        second_sample_observations[second_sample_observations.index(copy[i])] = 'Done'
