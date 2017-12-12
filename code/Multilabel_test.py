from DatabaseExtractor import *
from OutputGenerator import *

from sklearn.preprocessing import StandardScaler
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle

import numpy as np

# Read in the data of the match and of the players
"""
  input will be; for both Home and Away
  -Build-up-speed
  -Chance-creating-passing
  -Chance-creating-crossing
  -Chance-creating-shooting
  -defence-pressure
  -defence-Aggression
  -defence-pressure
  -defence-width
"""
from DatabaseExtractor import *
from sklearn.preprocessing import StandardScaler
from sklearn.multiclass import OneVsRestClassifier
from OutputGenerator import *
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier


# Read in the data of the match and of the players
x2 = read_data("Match", "home_player_1")[:1000]
x3 = read_data("Match", "home_player_2")[:1000]
x4 = read_data("Match", "home_player_3")[:1000]
x5 = read_data("Match", "home_player_4")[:1000]
x6 = read_data("Match", "home_player_5")[:1000]
x7 = read_data("Match", "home_player_6")[:1000]
x8 = read_data("Match", "home_player_7")[:1000]
x9 = read_data("Match", "home_player_8")[:1000]
x10 = read_data("Match", "home_player_9")[:1000]
x11 = read_data("Match", "home_player_10")[:1000]
x12 = read_data("Match", "home_player_11")[:1000]

p1_rating = stats_from_id(x2, "overall_rating", [67])
p2_rating = stats_from_id(x3, "overall_rating", [70])
p3_rating = stats_from_id(x4, "overall_rating", [70])
p4_rating = stats_from_id(x5, "overall_rating", [70])
p5_rating = stats_from_id(x6, "overall_rating", [70])
p6_rating = stats_from_id(x7, "overall_rating", [70])
p7_rating = stats_from_id(x8, "overall_rating", [70])
p8_rating = stats_from_id(x9, "overall_rating", [70])
p9_rating = stats_from_id(x10, "overall_rating", [70])
p10_rating = stats_from_id(x11, "overall_rating", [70])
p11_rating = stats_from_id(x12, "overall_rating", [70])


rating=[]
for i in range(len(x2)):
    rating.append([p1_rating[i][0], p2_rating[i][0], p3_rating[i][0], p4_rating[i][0], p5_rating[i][0], p6_rating[i][0], p7_rating[i][0], p8_rating[i][0], p9_rating[i][0], p10_rating[i][0], p11_rating[i][0]])

print(rating)
y = process_output()

# split into training and test
x_train = (rating[:800])
y_train = (y[:800])
x_test = (rating[800:1000])
y_test = (y[800:1000])


forest = RandomForestClassifier(n_estimators=1000, max_features=None, max_depth= None,  min_samples_split= 2, min_samples_leaf=100)
#multi_target_forest = MultiOutputClassifier(forest, n_jobs=1)
result = forest.fit(x_train, y_train)
result = forest.predict(x_test)
score = forest.score(x_test, y_test)
#print(y_test)
print(result)

print(x_test)
print(score)
