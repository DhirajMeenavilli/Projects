# Data Integerity

Data may be structured the way it is for multiple reasons, thus there are many meta things to think about and explore about the data itself, for example:

1. Some features are not recorded, because of stigma, incompetence, lack of strict relevance, budgetry constraints etc. Which is remedied by thinking what data would be available to the recorder/publisher at a given moment in time, and how it may perhaps could be latent in the currently provided data.

2. Some observations have their feature values distorted in one direction or another, for example income and balance sheets due to changes in GAAP, changes in the kind of GAAP used, or simply poor internal controls, the only way to remedy this is to look at the other feature values of a given observation and try to spot any distortitions that don't quite align i.e. accounting

3. The data may be complete, but not generalisable i.e. no more houses are being built in the area from which you are pulling sample data, and you are trying to predict on a neighboring area, the only solution is to account for potential drift in the time since.

4. The data may be incomplete, to which the only solution is collecting and cleaning the data.

5. The data may have target leakage, as in one of the features available during training won't be available during deployment and prediction time. The data may also have train-test contimanation where, the test data has already been fit to virtue of preprocessing done prior to splitting the data into train and test.