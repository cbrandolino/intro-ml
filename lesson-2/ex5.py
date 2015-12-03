# Optimize C Parameter

from sklearn.svm import SVC

c_values = [10.0, 100.0, 1000.0, 10000.0]

for c in c_values:
    clf = SVC(kernel='rbf', C=c)
    clf.fit(features_train[:len(features_train)/100], labels_train[:len(labels_train)/100])
    print "C: {0}, score: {1}".format(c, clf.score(features_test, labels_test))