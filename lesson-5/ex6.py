# Dealing with Unfilled Features

import pickle

enron_data = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r"))

print sum(1 for x in enron_data.values() if x['salary'] != 'NaN')
print sum(1 for x in enron_data.values() if x['email_address'] != 'NaN')
