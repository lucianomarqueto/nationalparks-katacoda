from __future__ import print_function

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
    return 'Welcome to the National Parks data service.'
