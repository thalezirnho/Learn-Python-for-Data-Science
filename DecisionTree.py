# Code for Decision Tree

# Code by Thales Follador de Oliveira
# e-mail: thalesfollador@gmail.com
# Code based on Learn Python for Data Science - by Siraj Raval

# Importing Decision Tree from Scikit Learn
from sklearn import tree

# Creating classifier
classifier = tree.DecisionTreeClassifier()

# Features = [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# Reference to each feature 
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# Training our data
classifier = classifier.fit(X, Y)

# Predicting gender for following features
prediction = classifier.predict([[190, 70, 43]])

# Printing the prediction
print(prediction)