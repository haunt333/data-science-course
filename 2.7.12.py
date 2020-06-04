import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV


X_train = train.drop(['y'], axis='columns')
y_train = train.y
parameters = {'max_depth': range(1,11), 'min_samples_split': range(2,11),'min_samples_leaf':range(1,11)}
dt = DecisionTreeClassifier()
search = GridSearchCV(dt, parameters, cv=5)
search.fit(X_train, y_train)
best_tree = search.best_estimator_
predictions = best_tree.predict(test)
