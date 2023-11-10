# When dealing with a new dataset, or even a dataset you've run some preliminary trials on for finding predictivness etc. you may have 100's or thousands of latent combination features or improperly procesed features of the variable in question.

# A good first step is to begin with a feature utility metric. As the name implies it's a metric which we can use to model how valuable a given feature is in helping us predict. 

# Thus comes about Mututal Information, which purportedly is computationally efficient, theoretically well founded, easy to use, and can detect any kind of relationship not just linear.

# Mututal Information describes relationships in terms of uncertainity. The MI is thus interperted as how much is uncertainity about a a given variable y, reduced by knowing inofrmation about a given varaible, x. 


### Extra Thoughts:

# Obviously though Celcius and Farenheight may be both be valuable indicators of how predictive a feature is but they give no new information in the Shannon sense to the model about the prediction.

# Mutual information if it's 1 between 2 features is probably a good indicator that you're not getting any new information to predict with when you do your prediction considering both as opposed to just considering one.