# Deploying a Training/Testing Regime

#### Boilerplate #################################################################

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r") )

features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

#### Exercise code #############################################################

from sklearn import tree
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)