# Decision tree accuracy

from sklearn import tree 

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

acc = clf.score(features_test, labels_test)