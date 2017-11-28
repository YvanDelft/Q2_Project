#import numpy as np
#import sklearn
#from sklearn import preprocessing
#from sklearn.linear_model import LogisticRegression

#LogisticRegression()

from sklearn.preprocessing import MultiLabelBinarizer
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]
print(MultiLabelBinarizer().fit_transform(y))
#array([[0, 0, 1, 1, 1],
#       [0, 0, 1, 0, 0],
#       [1, 1, 0, 1, 0],
#       [1, 1, 1, 1, 1],
#       [1, 1, 1, 0, 0]])
