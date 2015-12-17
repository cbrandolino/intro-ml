# Finding POIs

import pickle

enron_data = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r"))

print sum(1 for x in enron_data.values() if x['poi'] == True)