# Missing POIs 1

import pickle

enron_data = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r"))

print sum(1 for x in enron_data.values() if x['total_payments'] == 'NaN') * 100 / len(enron_data)
