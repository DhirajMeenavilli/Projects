# When looking at any data you should first and foremost ask yourself can I even do what I'm trying to do here. Is this something I in my position as a person with all my connections is this something I can even do assuming the features or collection tehniques may be slightly or wholly wrong or decieving.

import numpy as np
import pandas as pd
import random

# 1.  Data is based on past observations. It's backward-looking, and it assumes that the future will resemble the past. However, this assumption can be flawed, particularly when dealing with rare and extreme events that haven't occurred in the historical record.

store = []

random_numbers = np.random.normal(3, 14, 1000)

df = pd.DataFrame({'RandomNumber': random_numbers})

print(df.describe()) # Even with it holding that the past is exactly like the future i.e. they are generated from the exact same generator I would not in a 1000 samples be able to find any way to consistently profit, and/or take risks that could blow up on me in any way and not have had a death inducing failure.

# I wonder though if a RL model could learn what generator was producing what number and what number it is likely going to produce. The distance being the reward and maximisation would be zero error. I wonder if there's an RL model library from which I could import all sorts of models and just run the exzpiriment on.

# 2. Should be aware of the concept of "silent evidence." Data often omits information about what didn't happen or entities that failed. Survivorship bias is a common issue; it can lead us to overly optimistic conclusions about the potential for success.

intial_wallets = np.full(10000,10000) # Intialises 10,000 inddividuals with 1000 dollars

random_numbers = np.random.normal(20, 25, 100)

result = np.empty_like(intial_wallets)

for i in range(len(intial_wallets)):

    # Randomly sample a subset of arr2
    # timeInvested = abs(int(random.gauss(35, 5)))

    subset = np.random.choice(random_numbers, size=9, replace=False)  # Adjust the size as needed
    
    # Multiply the element in arr1 by the product of the sampled subset
    
    result[i] = intial_wallets[i] * np.prod(subset)

df = pd.DataFrame({'End Results': random_numbers})
print()
print(df.describe()) # Even with relatively small multipliers and short time period, even the 3rd quartile is only 38x with very few around the 100x level, and we'd only even record people probably above the 40-50x level, and so it becomes a very small population, and in that we also only focus more and 
# more at the most successful resulting in an almost n = 1 situation or even just n = 100 or n = 500 and we end up with phrases like, "Well someone has to be the next Buffett." or "Value Investors can do it look at all these examples." or "Look How many people from so many styles make it so big."
# When even like 10000 people started.

# 3. The time frame of the data matters. Short-term data may not reflect the long-term dynamics of a system. For this one it onl goes 9 years

# 4. Data can be noisy, inaccurate, or subject to manipulation. If the data source is unreliable or biased, it can lead to incorrect conclusions.

# 5. The data may not capture "unknown unknowns." These are the events or factors that we can't even conceive of because they've never happened before. No amount of historical data can prepare us for these unexpected events.
print(1000) # Imagine this but all of the systems are built on the premise this can't happen.