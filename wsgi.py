# from __future__ import print_function

# import os
# import json

# from flask import Flask, request
# from flask_restful import Resource, Api

# application = Flask(__name__)

# api = Api(application)

# class Hello(Resource):
#     def get(self):
#         return 'Hello World'

# api.add_resource(Hello, '/ws/hello/')

# @application.route('/')
# def index():
#     return 'Welcome to the National Parks data service.'

# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0')

# load Flask 
import flask
app = flask.Flask(__name__)
# define a predict function as an endpoint 
@app.route("/predict", methods=["GET","POST"])
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
# start the flask app, allow remote connections
app.run(host='0.0.0.0')