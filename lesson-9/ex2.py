# Computing Rescaled Features

#### Boilerplate #################################################################

import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()

data_dict = pickle.load( open("../ud120-projects/final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)

#### Exercise code #############################################################

from sklearn.preprocessing import MinMaxScaler

feature_1 = "salary"
feature_2 = "exercised_stock_options"
features_list = [feature_1, feature_2]
data = featureFormat(data_dict, features_list )

def scale(arr, value):
    scaler = MinMaxScaler()
    scaler.fit(arr)
    return scaler.transform([float(value)])[0] 

print scale([item[0] for item in data], 200000)
print scale([item[1] for item in data], 1000000)


#### Boilerplate #################################################################
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
