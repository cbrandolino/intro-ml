# Follow the money

import pickle

enron_data = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r"))

print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['SKILLING JEFFREY K']['total_payments']
