# Accuracy of Naive Bayes

from sklearn.naive_bayes import GaussianNB

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    clf = GaussianNB()
    pred = clf.fit(features_train, labels_train)
    accuracy = clf.score(features_test, labels_test)
    return accuracy