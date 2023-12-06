# Attention can be terrifying, how can we retain our privacy?
# An exploration into if the capabilitys exist to dictate your political leanings from a simple picture. 
# IF yes, then 
# 1) Look for reasons why you could have gotten your result and disconfirm all that you can with the given resources etc. 
# that could provide an alternative explination of why you got a Positive. More simply discofirm a false positive as much as you can.
# What you can't do, put for the next people who care enough to try with more resources and if they can disconfirm further hypothesis, 
# we could have more confidence, or a very new interesting question to explore.
#
# 2) Figure out what you can do to throw the model of heuristically, and that's another expiriment. So, it becomes like 2 papers.
# Which is better, even if it's more disatisfying.

# Expiriment 1 - Part 1
#
#    Dataset: 
#       Liberal and Conservative MPS from the Canadian Government of 2023.
#   
#   Apriori:
#       There are facial charachteristics that dictate the political leanings of an 
#       individual, though those charachteristics may be highly varied and dependant 
#       on time and geographic contexts.
#
#    Potential Reasons for Failure (Factors to Disprove before saying it's not doable):
#       Data Size Insufficiency (Progressive Steps: A few other prior parliments, all prior parliments, 
#       other countries few then many, and if someone wants to go further they can try with labelling pictures from social media etc.)
#
#       Feature Insufficiency [Due to bias in the data possibly](Gender is unrepresentative of the genreal population (Male mostly), 
#       Age is unrepresentative of the general population (Mostly old), Race is unrepresentative of the general population to a very
#       extereme extent (Mostly white), Class is very unrepresentative of the general population (Mostly Rich)) [This is both a fun
#       excercise which can be extended to a fun activity for people to do, and also something if you make explicit, can allow you to
#       solve for where the predcition is really coming from allowing an easy lair of explainability, and finally making it easy to
#       come up with new hypothesis or links like can wealth be predicted from a picture good enough that it can determine your 
#       political leaning etc.]
#
#
#    Potential Reasons for Success (Factors to Disprove before saying it's doable):
#       Overly Specialized Data (Not representative so it works on this data but cracks on another)
#
#       Improper Metric of Success (A one time point estimate 
#       mean for a bimodal distribution of outcomes)
#       
#       It actually works (Never really provable)
# 
#    Impact:
#       Regulations likely needed (The ability and knowledge of how to opt out, most people prolly wouldn't care. 
#       But it'd be important to)

import fastai

# First thing I made sure of was that Conservative MPS and I hope this is true for the rest of the data, don't wear more blue ties
# Hopefully there's no trend of liberals wearing red things or wearing less blue or sumin. We'll see though.

# Might start with a desire to learn something like can political leanings be learnt from vision technologys observation of faces alone.
# And end up with the conclusion Liberal leaning MPs smile more in Canadian political display headshots than conservatives in whenever 
# the last election was.