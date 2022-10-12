from sklearn.linear_model import LinearRegression
import numpy as np
from joblib import dump, load
import os
path = os.getcwd()

print("Working directory: {}".format(path))

# mock data
X_train = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape((-1, 1))
y_train = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]).reshape((-1, 1))

# training model
model = LinearRegression()
model.fit(X_train, y_train)
model.score(X_train, y_train)

# persisting model
dump(model, '../models/reg_model.joblib')

# loading model
model_pers = load('../models/reg_model.joblib') 

# testing model
new_data = np.array([7, 28]).reshape((-1, 1))
print("Prediction for {} ===>>> {}".format(new_data, reg.predict(new_data)))