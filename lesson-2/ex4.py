# Deploy an rbf kernel

from sklearn.svm import SVC
clf = SVC(kernel='rbf')
clf.fit(features_train[:len(features_train)/100], labels_train[:len(labels_train)/100])
print clf.score(features_test, labels_test)