# Missing POIs 5

import pickle

enron_data = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r"))

pois = [x for x in enron_data.values() if x['poi'] == True]
pois_new_sum = len(pois) + 10
print pois_new_sum
print (sum(1 for x in pois if x['total_payments'] == 'NaN') + 10)
