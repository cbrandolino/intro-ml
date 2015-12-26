# Train/Test Split in sklearn

#### Boilerplate #################################################################

from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
features = iris.data

#### Exercise code #############################################################

from sklearn import cross_validation 
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

#### Boilerplate #################################################################

clf = SVC(kernel="linear", C=1.)
clf.fit(features_train, labels_train)

print clf.score(features_test, labels_test)

def submitAcc():
    return clf.score(features_test, labels_test)