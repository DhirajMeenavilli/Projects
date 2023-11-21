# It becomes a sort of quick iteration process, but it should be like mutual information telling you 
# where possibly good features to construct are, and then construcing features which we then test via MI

# To construct features there's a few things that can be done.

# 1. Mathematical Transforms (Add, Subtract, Divide, Multiply, Log, etc.)

"""
X_1["LivLotRatio"] = X["GrLivArea"] / X["LotArea"]
X_1["Spaciousness"] = (X["FirstFlrSF"]+X["SecondFlrSF"]) / X["TotRmsAbvGrd"]
X_1["TotalOutsideSF"] = X["WoodDeckSF"]+X["OpenPorchSF"]+X["EnclosedPorch"]+X["Threeseasonporch"]+X["ScreenPorch"]
"""

# 2. Taking counts of catergorical values.

"""

X_3["PorchTypes"] = df[["WoodDeckSF",
"OpenPorchSF",
"EnclosedPorch",
"Threeseasonporch",
"ScreenPorch"]].gt(0.0).sum(axis=1)

"""

# 3. Breaking down strings, for ex. (780) 438-2191 -> 780 so we can get an area code. Or like "Company L2" -> "Company" and "L2".

"""

X_4["MSClass"] = df.MSSubClass.str.split("_", n=1, expand=True)[0]

"""

# 4. Building up from Strings, "Alfa Romeo" "Convertible" -> "Alfa Romeo Convertible".
"""

X_4["LotShapeAlleyEntry"] = df.LotShape + ' ' + df.Alley

"""
# 5. Group Transforms such as Average income across states.

"""

X_5["MedNhbdArea"] = df.groupby("Neighborhood")["GrLivArea"].transform("median")

"""

# Additional Notes and Occurances.

"""
If you've discovered an interaction effect between a numeric feature and a categorical feature, you might want to model it explicitly using a one-hot encoding, like so:

# One-hot encode Categorical feature, adding a column prefix "Cat"
X_new = pd.get_dummies(df.Categorical, prefix="Cat")

# Multiply row-by-row
X_new = X_new.mul(df.Continuous, axis=0)

# Join the new features to the feature set
X = X.join(X_new)

    For example:

    # One-hot encode BldgType. Use `prefix="Bldg"` in `get_dummies`
    X_2 = pd.get_dummies(df.BldgType, prefix="Bldg")
    # Multiply
    X_2 = X_2.mul(X.GrLivArea, axis=0)

    X = X.join(X_2)
"""


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