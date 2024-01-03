import pandas as pd
### --- KMeans --- ###

### ---  PCA   --- ###

# Applied to standardised data hence, variation means correlation. If the data were unstandardised it would mean covariance.
# The whole idea of PCA: instead of describing the data with the original features, we describe it with its axes of variation. The axes of variation become the new features.

# The new features PCA constructs are actually just linear combinations (weighted sums) of the original features.

# These new features are called the principal components of the data. The weights themselves are called loadings. There will be as many principal components as there are features 
# in the original dataset: if we had used ten features instead of two, we would have ended up with ten components.

# It's important to remember, however, that the amount of variance in a component doesn't necessarily correspond to how good it is as a predictor: 
# it depends on what you're trying to predict.

"""
There are two ways you could use PCA for feature engineering.

The first way is to use it as a descriptive technique. Since the components tell you about the variation, you could compute the MI scores for the components and see what kind of variation is most predictive of your target. That could give you ideas for kinds of features to create -- a product of 'Height' and 'Diameter' if 'Size' is important, say, or a ratio of 'Height' and 'Diameter' if Shape is important. You could even try clustering on one or more of the high-scoring components.

The second way is to use the components themselves as features. Because the components expose the variational structure of the data directly, they can often be more informative than the original features. Here are some use-cases:

Dimensionality reduction: When your features are highly redundant (multicollinear, specifically), PCA will partition out the redundancy into one or more near-zero 
variance components, which you can then drop since they will contain little or no information.

Anomaly detection: Unusual variation, not apparent from the original features, will often show up in the low-variance components. 
These components could be highly informative in an anomaly or outlier detection task.

Noise reduction: A collection of sensor readings will often share some common background noise. PCA can sometimes collect the 
(informative) signal into a smaller number of features while leaving the noise alone, thus boosting the signal-to-noise ratio.

Decorrelation: Some ML algorithms struggle with highly-correlated features. PCA transforms correlated features into uncorrelated 
components, which could be easier for your algorithm to work with.

PCA basically gives you direct access to the correlational structure of your data.

There are a few things to keep in mind when applying PCA:

PCA only works with numeric features, like continuous quantities or counts. PCA is sensitive to scale. It's good practice to 
standardize your data before applying PCA, unless you know you have good reason not to.

Consider removing or constraining outliers, since they can have an undue influence on the results.
"""
Titanic_train = pd.read_csv('Would You Have Survived The Titanic/Models Training Passengers.csv')
Titanic_train.dropna(axis=1,inplace=True)

features = ["PassengerId", "SibSp", "Parch","Fare"]
X = Titanic_train.copy()
y = X.pop('Survived')
X = X.loc[:, features]

# Standardize
X_scaled = (X - X.mean(axis=0)) / X.std(axis=0)

from sklearn.decomposition import PCA

# Create principal components
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Convert to dataframe
component_names = [f"PC{i+1}" for i in range(X_pca.shape[1])]
X_pca = pd.DataFrame(X_pca, columns=component_names)

X_pca.head()

loadings = pd.DataFrame(
    pca.components_.T,  # transpose the matrix of loadings
    columns=component_names,  # so the columns are the principal components
    index=X.columns,  # and the rows are the original features
)

print(loadings)