from DatabaseExtractor import read_data
from sklearn.linear_model import LogisticRegression

data = read_data("player_attributes", "*")

solver = "saga"

n_samples = 1000
algorithm_parameters = "solver='saga', multi_class='multinomial'"

x_data = 1
y_data = 1


clf = LogisticRegression(algorithm_parameters)
clf.fit(x_data, y_data)
