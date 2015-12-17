# Query the dataset 1

import pickle

enron_data = pickle.load(open("../ud120-projects/final_project/final_project_dataset.pkl", "r"))

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
