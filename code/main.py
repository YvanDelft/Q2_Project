from DatabaseExtractor import *
from sklearn.preprocessing import StandardScaler
from sklearn.multiclass import OneVsRestClassifier
from OutputGenerator import *
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.svm import LinearSVC



# Read in the data of the match and of the players
x2 = read_data("Match", "home_player_1")
p1_rating = stats_from_id(x2, "overall_rating", 50)
print(p1_rating)
print(len(p1_rating))


y = process_output()

# split into training and test
x_train = p1_rating[:800]
y_train = y[:800]
x_test = p1_rating[800:1000]
y_test = y[800:1000]

#scaler = StandardScaler()

# Apply linear regression models [MODELS ARE VERY BAD ATM]
algorithm_parameters = "solver='lbfgs', multi_class='multinomial'"
clf = OneVsRestClassifier(LogisticRegression())
result1=clf.fit(x_train, y_train).predict(x_test)

otherclf= LogisticRegression()
result2 = otherclf.fit(x_train,y_train).predict(x_test)

print(result1)
print(result2)

