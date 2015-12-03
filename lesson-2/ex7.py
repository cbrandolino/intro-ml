# Extracting Predictions from an SVM

from sklearn.svm import SVC

clf = SVC(kernel='rbf', C=100)
clf.fit(features_train[:len(features_train)/100], labels_train[:len(labels_train)/100])
predictions = clf.predict(features_test)

for pred_index in [10, 26, 50]:
  print "{0}: {1}".format(pred_index, predictions[pred_index])