# Author ID accuracy

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
pred = clf.fit(features_train, labels_train)
accuracy = clf.score(features_test, labels_test)
print accuracy