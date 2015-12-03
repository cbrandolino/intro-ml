# Timing Your NB Classifier

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"