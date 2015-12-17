#  Decision Tree Accuracy Quiz

from sklearn import tree 

clf = tree.DecisionTreeClassifier(min_samples_split=2)
clf.fit(features_train, labels_train)
acc_min_samples_split_2 = clf.score(features_test, labels_test)

clf = tree.DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train, labels_train)
acc_min_samples_split_50 = clf.score(features_test, labels_test)