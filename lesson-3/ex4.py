# Your first email DT: Accuracy 

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree 

features_train, features_test, labels_train, labels_test = preprocess()

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)