# SVM Author ID Accuracy

from sklearn.svm import SVC
clf = SVC(kernel='linear')
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)