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
        temp_counter += 1
        if temp_counter < 200:
            path = os.path.join('../ud120-projects/', path[:-1])
            email = open(path, "r")
            
#### Exercise code #############################################################

            text = parseOutText(email)
            taboo = ["sara", "shackleton", "chris", "germani"]
            purified_text = ' '.join([word for word in text.split() if word not in taboo])
            word_data.append(purified_text)
            from_data.append( 0 if (name == 'sara') else 1)

#### Boilerplate #################################################################

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

print word_data[152]
pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here


