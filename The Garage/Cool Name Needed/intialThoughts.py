"""
Name: Bayes Detector
Author: Dhiraj Meenavilli
Date: 11/16/2023
"""

# It's effectively going to be a Geiger counter but for statistical waste (poor distributional consideration and preperation).
# A sort of statistical Goodness of Fit test, but by using brute force and Bayes theorem.
# This I believe can be achieved by doing the following:

# 1. Set up a random distribution with some random parameter values, 

# 2. Then start getting it to spit out values.

# 3. Create a Bayes machine which outputs the proability of a given distribution with certain parameter values.

# I.e. Gaussian with u = 100 and s.d. = 10 vs. Gaussian with u = 20 and s.d. = 5 vs. Cauchy with lambda = 2 and Xnot = 4 etc.
# From this eliminate unlikelys over a stream of observations and then this can do 3 things:

# 1) Tell us how many observations we need to eliminate a distribution on average (possibly).
# 2) Tell us what we can and cannot intelligently say given a set of observations which are neccessarily in sample and thus a function of luck.
# 3) Tell us which distributions we could possibly consider and thus with tools to avoid and which to bring.

# stat.rv_continuous is for unvariate statistical distributions and there's like 50 some, 
# then there's 16 multivariates hence why saying what it is is near impossible, but saying what it isn't is quite simple
# It would suffer from so much overfitting with so many models to fit with. # Part 1 possible useful contribution.

# Hence why using something like a discrete number of possible models even if it's a few million or billion or trillion is not a problem 
# As the aggreagate % of surviving models after the full stream of observations, which if above a good threshold say > 5%, should suffice in considering that distribution as valid.
# Then if there is low variance amojng the parameters of the distribution we could say maybe those are appropriate aprameters to consider and do further testing. # Potentail Contribution 2

# This idea could be problematic if few of the right distribution say the power law survive due to the fact small shifts in parameter value can make the likelihoods far lower
# Hence appropriate discretisation is very very important.

# import matplotlib.pyplot as plt If you ever want to plot the outcomes.
from scipy.stats import norm, powerlaw # import basically all distributions.

# Define the values to check probability for
mean = 0
std_dev = 1
num_samples = 10

# Generate random numbers
values_to_check = norm.rvs(loc=mean, scale=std_dev, size=num_samples).tolist()

# Parameters for different distributions
gaussian_mean_1 = 10 # Write a loop to create the appropriate discrete instances of various distributions, which the computer can then quickly check through and eliminate some and keep others.
gaussian_std_dev_1 = 20

gaussian_mean_2 = 15
gaussian_std_dev_2 = 10

power_law_lambda = 2
power_law_x0 = 4

true_gaussian = mean
true_gaussian_std_dev = std_dev

# Compute probabilities for each value from different distributions
probabilities = {
    'Gaussian_1': norm.pdf(values_to_check, loc=gaussian_mean_1, scale=gaussian_std_dev_1),
    'Gaussian_2': norm.pdf(values_to_check, loc=gaussian_mean_2, scale=gaussian_std_dev_2),
    'PowerLaw': powerlaw.pdf(values_to_check, power_law_lambda, loc=power_law_x0),
    'True Gaussian': norm.pdf(values_to_check, loc=true_gaussian, scale=true_gaussian_std_dev)
}

# Print probabilities
for value in values_to_check:
    print(f"Value: {value}")
    for dist_name, prob in probabilities.items():
        print(f"{dist_name}: {prob[values_to_check.index(value)]}")

