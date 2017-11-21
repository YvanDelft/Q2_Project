from DatabaseExtractor import read_data
from sklearn.linear_model import LogisticRegression

data = read_data("player_attributes", "*")

solver = "saga"

n_samples = 1000
algorithm_parameters = "solver='saga', multi_class='multinomial'"

x = 1
y = 1

x_train =
y_train =
x_test =
y_test =

scaler = StandardScaler()


clf = LogisticRegression(algorithm_parameters)
clf.fit(x_data, y_data)
