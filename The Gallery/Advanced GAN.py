# We use Wasserstein Loss as it is better at avoiding mode collapse (i.e. getting stuck at one point in the distribution)
# Also the loss value is not really 1:1 in any capacity between BCE and the quality of image
# Also the BCE Loss has a sigmoidal change from the top intially meaning the graddient is very flat hence pulling the distribution of the two together becomes slow and difficult.
# Wasserstein uses something called Earth Mover Distance, i.e. the effort taken to pull the distribution together, this is done by unrestricting the critic/classifier so it can be between 1 and -1
# it also leads to a more linear loss, hence better gradients.
# The Wasserstein condition which additionally to using Earth Mover Loss, is using 1-Lipschitz continous condition is that the norm of the gradient of the critic is 1 or less at any point.
# This stabalises training, and prevents gradients from exploding.
# This is achieved by either clipping the weights post update (which can lead to some ugly results) or simply applying a regularization.
# The regularization in this case is just lambda * gradinent penalty factor.
# The gradient penalty is then the norm of the gradient of the critic for a set of real and fake images - 1 and then squared.
# This then being applied to the critic loss, means the critic algorithim actively tries to lower the gradients so that the Lipschitz rule can be enforced.