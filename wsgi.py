''' from __future__ import print_function

import os
import json

from flask import Flask, request
from flask_restful import Resource, Api

application = Flask(__name__)

api = Api(application)

class Hello(Resource):
    def get(self):
        return 'Hello World'

api.add_resource(Hello, '/ws/hello/')

@application.route('/')
def index():
    return 'Welcome!!!.'

if __name__ == '__main__':
    application.run(debug=False, host='0.0.0.0')
 '''
''' 
import flask
application = flask.Flask(__name__)
# define a predict function as an endpoint 
@application.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}
    # get the request parameters
    params = flask.request.json
    if (params == None):
        params = flask.request.args
    # if parameters are found, echo the msg parameter 
    if (params != None):
        data["response"] = params.get("msg")
        data["success"] = True
    # return a response in json format 
    return flask.jsonify(data)

@application.route('/')
def index():
    return 'Welcome back!!!.'

# start the flask app, allow remote connections
if __name__ == '__main__':  
    application.run(host='0.0.0.0')

 '''
# Load libraries
import flask
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model

# instantiate flask 
application = flask.Flask(__name__)

# we need to redefine our metric function in order 
# to use it when loading the model 
def auc(y_true, y_pred):
    auc = tf.metrics.auc(y_true, y_pred)[1]
    keras.backend.get_session().run(tf.local_variables_initializer())
    return auc

# load the model, and pass in the custom metric function
global graph
graph = tf.get_default_graph()
model = load_model('games.h5', custom_objects={'auc': auc})

# define a predict function as an endpoint 
@application.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, return a prediction
    if (params != None):
        x=pd.DataFrame.from_dict(params, orient='index').transpose()
        with graph.as_default():
            data["prediction"] = str(model.predict(x)[0][0])
            data["success"] = True

    # return a response in json format 
    return flask.jsonify(data)    

@application.route('/')
def index():
    return 'Welcome back and back!!!.'

# start the flask app, allow remote connections
if __name__ == '__main__':  
    application.run(host='0.0.0.0')
