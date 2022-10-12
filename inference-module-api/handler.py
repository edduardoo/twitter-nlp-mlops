import json
import boto3
import numpy as np
from sklearn.linear_model import LinearRegression
import numpy as np
from joblib import dump, load
import json


def handler(event, context):
    #body = event["body"]
    #if type(body) == str: # locally is a dict but on API Gateway is a string
     #   body = json.loads(body)

    print("EVENT PARAMS: {}".format(event))
    print("EVENT TYPE: {}".format(type(event)))
    inp = event["Input"]
    if type(inp) == str: # locally is a dict but on API Gateway is a string
        inp = json.loads(inp)

    #new_data = np.array(body["Input"]).reshape((-1, 1))
    new_data = np.array(inp).reshape((-1, 1))

    # loading model
    model = load('./reg_model.joblib') # at run time, the model is in the same folder as the handler in the container
    
    # predicting
    pred = model.predict(new_data)

    # preparing response json
    response = {'predictions': list(pred.reshape(-1))}
    response = json.dumps(response)

    return {
        'statusCode': 200,
        'body': response
    }


def train():
    # mock data
    X_train = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape((-1, 1))
    y_train = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]).reshape((-1, 1))

    # training model
    model = LinearRegression()
    model.fit(X_train, y_train)
    model.score(X_train, y_train)

    # persisting model
    dump(model, './models/reg_model.joblib')

    # loading model
    model_pers = load('./models/reg_model.joblib') 

    # testing model
    new_data = np.array([7, 28]).reshape((-1, 1))
    print("Prediction for {} ===>>> {}".format(list(new_data), list(model_pers.predict(new_data))))


# the model is trained locally, by runing "python handler.py"
if __name__ == "__main__":
   train()