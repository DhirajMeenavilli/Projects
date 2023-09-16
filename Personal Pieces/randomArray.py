import random

def randomArray(arr: []) -> []:
    arr = random.shuffle(arr)[0:random.randint(1,len(arr))]
    return arr
