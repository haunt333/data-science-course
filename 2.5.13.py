import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split

clf = DecisionTreeClassifier(max_depth = 101, random_state=42)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
precision = precision_score(y_test, predictions, average='micro')
