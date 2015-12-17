# Size of the enron dataset

import pickle

enron_data = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r"))

print len(enron_data)