#!/usr/bin/python

#### Boilerplate #################################################################

import os
import pickle
import re
import sys

sys.path.append( "./" )
from ex2 import parseOutText

from_sara  = open("../ud120-projects/text_learning/from_sara.txt", "r")
from_chris = open("../ud120-projects/text_learning/from_chris.txt", "r")

from_data = []
word_data = []
temp_counter = 0

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:

        path = os.path.join('../ud120-projects/', path[:-1])
        email = open(path, "r")

#### Exercise code #############################################################

        text = parseOutText(email)
        taboo = ["sara", "shackleton", "chris", "germani"]
        for word in taboo:
          text = text.replace(word, '')
        word_data.append(text)
        from_data.append( 0 if (name == 'sara') else 1)
        email.close()

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)
vectorizer.fit_transform(word_data)
print len(vectorizer.get_feature_names())

#### Boilerplate #################################################################

from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here


