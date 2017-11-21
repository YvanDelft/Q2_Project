from DatabaseExtractor import read_data
from sklearn.linear_model import LogisticRegression
import sklearn
from OutputGenerator import *

data = read_data("match", "home_team_goal, away_team_goal")

bet365 = "B365H, B365D, B365A"
blue_square = "BSH, BSD, BSA"
gamebookers = "GBH, GBD, GBA"
interwetten = "IWH, IWD, IWA"
ladbrokes = "LBH, LBD, LBA"
pinnacle = "PSH, PSD, PSA"
sporting_odds = "SOH, SOD, SOA"
sportingbet = "SBH, SBD, SBA"
stan_james = "SJH, SJD, SJA"
stanleybet = "SYH, SYD, SYA"
vc_bet = "VCH, CCD, VCA"
william_hill = "WHH, WHD, WHA"


solver = "saga"

n_samples = 1000

print(data)

#print(process_betting_odds(bet365))
#print(process_betting_odds(william_hill))


#x_data =
#y_data =

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
