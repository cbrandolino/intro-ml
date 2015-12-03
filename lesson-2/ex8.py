# How Many Chris Emails Predicted?

from sklearn.svm import SVC

clf = SVC(kernel='rbf', C=10000.0)
clf.fit(features_train[:len(features_train)], labels_train[:len(labels_train)])
predictions = clf.predict(features_test)
predictions_chris = filter(lambda x: x == 1, predictions)
print len(predictions_chris)
