# Optimized RBF vs. Linear SVM: Accuracy

from sklearn.svm import SVC

clf = SVC(kernel='rbf', C=10000.0)
clf.fit(features_train[:len(features_train)], labels_train[:len(labels_train)])
print clf.score(features_test, labels_test)