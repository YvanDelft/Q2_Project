from DatabaseExtractor import read_data

data = read_data("player", "birthday, height")
print(data[5])
