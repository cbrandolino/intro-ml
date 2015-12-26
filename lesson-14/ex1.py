# All exercises here

#### Boilerplate #################################################################

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r") )

features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn import tree
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

#### Exercise code #############################################################

from sklearn import metrics

prediction = clf.predict(features_test, labels_test)
pois_in_test = sum(prediction)
test_datapoints = len(prediction)


print "pois in test:", pois_in_test
print "test datapoints:", test_datapoints

print "IF 0 WERE PREDICTED FOR ALL DATA POINTS"
all_false_predictions = [0.] * test_datapoints
print "accuracy of classifier:", (test_datapoints - pois_in_test) / test_datapoints
print "precision of classifier", metrics.precision_score(prediction, all_false_predictions)
print "recall of classifier", metrics.recall_score(prediction, all_false_predictions)

print "WITH EXAMPLE PREDICTIONS"
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

from operator import add

pred_positives_num = sum(predictions)
pred_negatives_num = len(predictions) - pred_positives_num
true_positives = filter(lambda x: x == 2, map(add, predictions, true_labels))
true_negatives = filter(lambda x: x == 0, map(add, predictions, true_labels))
true_positives_num = len(true_positives)
true_negatives_num = len(true_negatives)
false_positives_num = pred_positives_num - true_positives_num
false_negatives_num = pred_negatives_num - true_negatives_num
print "total true positives", true_positives_num
print "total true negatives", true_negatives_num
print "total false positives", false_positives_num
print "total false negatives", false_negatives_num
print "precision", float(true_positives_num) / (true_positives_num + false_positives_num)
print "recall", float(true_positives_num) / (true_positives_num + false_negatives_num)

