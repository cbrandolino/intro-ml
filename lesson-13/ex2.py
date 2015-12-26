# Your First (Overfit) POI Identifier

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

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.score(features, labels)