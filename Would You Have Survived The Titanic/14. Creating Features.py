# It becomes a sort of quick iteration process, but it should be like mutual information telling you 
# where possibly good features to construct are, and then construcing features which we then test via MI

# To construct features there's a few things that can be done.

# 1. Mathematical Transforms (Add, Subtract, Divide, Multiply, Log, etc.)

# 2. Taking counts of catergorical values.

# 3. Breaking down strings, for ex. (780) 438-2191 -> 780 so we can get an area code. Or like "Company L2" -> "Company" and "L2".

# 4. Building up from Strings, "Alfa Romeo" "Convertible" -> "Alfa Romeo Convertible".

# 5. Group Transforms such as Average income across states.

"""
Tips on Creating Features
It's good to keep in mind your model's own strengths and weaknesses when creating features. Here are some guidelines:

    Linear models learn sums and differences naturally, but can't learn anything more complex.
    
    Ratios seem to be difficult for most models to learn. Ratio combinations often lead to some easy performance gains.

    Linear models and neural nets generally do better with normalized features. Neural nets especially need features scaled to 
    values not too far from 0. Tree-based models (like random forests and XGBoost) can sometimes benefit from normalization, but 
    usually much less so.

    Tree models can learn to approximate almost any combination of features, but when a combination is especially important they can still benefit from having it 
    explicitly created, especially when data is limited.
    
    Counts are especially helpful for tree models, since these models don't have a natural way of aggregating information across many features at once.
"""