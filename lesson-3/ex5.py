# Count 'Em Features

import sys
sys.path.append("../tools/")
from email_preprocess import preprocess

features_train, features_test, labels_train, labels_test = preprocess()

print len(features_train[0])