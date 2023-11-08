# Pipelines are a simple way to keep your data preprocessing and modeling code organized. Specifically, a pipeline bundles preprocessing and modeling steps so you can use the whole bundle as if it were a single step.

# Many data scientists hack together models without pipelines. But pipeline benifits include
import pandas as pd

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')
y = Titanic_train.Survived
X = Titanic_train.drop(['Survived'], axis=1) # Have to put wether the drop is in columns or rows otherwise the assumption is rows

from sklearn.model_selection import train_test_split

X_train, X_valid, y_train, y_valid = train_test_split(X,y)

lowOrdinalCatCols = [col for col in X_train.columns if X_train[col].dtype == 'object' and X_train[col].nunique() < 10] # It's creating an array by checking if the column is of type object and then if the number of uniques is less than 10, because that way you're only going to encode those low ordinality columns.
# Also copying code is fine if you do it by hand and comment on why the code is working.

numericalCols = [col for col in X_train.columns if X_train[col].dtype == 'int64' or X_train[col].dtype == 'float64'] # Intresting to note passangerId is caught here, which means it's a numerical type even though it should be a object type. It actually wasn't I made a mistake, but that doesn't change you should always double check it.

my_cols = lowOrdinalCatCols + numericalCols # Keeping only the low cardinality and numberical columns, these columns can still have NaN values and the catergorical data is not yet transformed only selected prior to any real processing.

X_train_final = X_train[my_cols]
X_valid_final = X_valid[my_cols]

#1. Cleaner Code: Accounting for data at each step of preprocessing can get messy. With a pipeline, you won't need to manually keep track of your training and validation data at each step.

from sklearn.compose import ColumnTransformer # Bundles together preprocessing steps
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

imputer = SimpleImputer(strategy='constant') # Constant lets you replace with any given fill value by default it's 0, it can also apply to catergorical variables but we would use this for numerical data only so we don't need to worry too much about that.

catergorical_tranformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')), # Steps: List of (name, transform) tuples (implementing fit/transform) that are chained, in the order in which they are chained, with the last object an estimator.
                                          ('onehot', OneHotEncoder(handle_unknown='ignore'))]) 

pre_processor = ColumnTransformer(transformers=[('num', imputer ,numericalCols), ('cats', catergorical_tranformer, lowOrdinalCatCols)]) # List of (name, transformer, columns) tuples specifying the transformer objects to be applied to subsets of the data.

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 100, random_state = 42)

from sklearn.metrics import accuracy_score
my_pipeline = Pipeline(steps=[('Preprocessor', pre_processor), ('model', model)])
my_pipeline.fit(X_train_final, y_train)

preds = my_pipeline.predict(X_valid_final) # Using this you don't need to run the preprocessing and all that again you just litterally build and use the pipeline. That's very cool, very plug and play.
print("Accuracy: ", accuracy_score(y_valid, preds)) # Just from this got 84%, ususally around 50-70%

#2. Fewer Bugs: There are fewer opportunities to misapply a step or forget a preprocessing step.

#3. Easier to Productionize: It can be surprisingly hard to transition a model from a prototype to something deployable at scale. We won't go into the many related concerns here, but pipelines can help.

#4. More Options for Model Validation: You will see an example in the next tutorial, which covers cross-validation.
