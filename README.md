# Minorproject
Objective:
This repository uses data about soccer matches to predict the outcome of soccer matches that haven't been played yet.
Using data about the players and the formation of both the home and away team and the history of earlier matches played between these teams,
an outcome of a match is being predicted. Using an artificial neural network, available data is being used to train the weights of this ANN,
which outputs the outcome of the match. Different kinds of input will be used to figure out which kind of input works the best for predicting soccer matches.
Also the predictions will be compared to the predictions of betting companies to find out if an ANN can produce predictions that are more accurate.

If a neural network can be created that has the ability to predict the outcomes accurately enough, 
this can be very useful to clubs all around the world to figure out the best formation or et of players for the upcomming match.
For example the neural network might show that Manchester City loses often from teams that have a 4-4-2 formation.
Also people that want to bet on matches will have a great overview of who to bet on. 
Thirdly the betting companies could make use of the ANN to put better profit margins  on the betting choices.

Data sources:
As much data as possible can be useful for training the neural network and predicting match-outcomes. 
The most important data will be a lot of matches that have been played and their outcomes, because this will be the expected output.
Also, at least one input variable is needed to make the network do its job. Any kind of input variable would suffice.
Examples are: the formations of the teams, the home and away configurations. The players that took part in the match, the average rating of the teams, etc.
A lot of these data can be found on kaggle. Also the game fifa can support much of the needed information.

Tools:
To process the data that has been achieved, a python program is needed to put the data into the right format. Also outliers should be removed.
Then a neural network will have to be created in python to generate output and predict the outcomes.
Lastly a prediction tool has to be created for users to give input and recive a prediction from the ANN.
