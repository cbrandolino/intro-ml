# Salary Range

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
from IPython import embed

features_list = ['salary']
data = featureFormat(data_dict, features_list )
flat_data = [item for sub in data for item in sub if item != 0]
print max(flat_data)
print min(flat_data)

#### Boilerplate #################################################################
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
