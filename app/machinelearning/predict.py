from flask import Flask, request, jsonify, render_template
from voluptuous import Schema, MultipleInvalid
import pandas as pd
import sklearn
from app.machinelearning.datamodel import datamodel


def predict(model_name):
    """ Main function. Predict house price given a set of input data and a
        stored model. Return a json struct"""

    dm = datamodel()

    # Get input parameters
    input_ok, data = fetch_input()
    if not input_ok:
        return 'Error: %s' % data

    # Import the trained model from the jupyter session
    model = dm.load_model(model_name)
    if not model:
        return 'Error: Could not load model'

    # The model needs the input data in a pandas dataframe. Pass array with headers
    # ensures correct estimate
    headers = dm.headers()
    input_data = pd.DataFrame([data])

    # Now run a prediction given on the trained model with the input data
    prediction = model.predict(input_data[headers])

    # Return a json structure containing input and resulting prediction
    ret = {'input': data,
           'model': model_name,
           'prediction': "%.2f" % prediction[0]}
    return ret


def fetch_input():
    """ Handle input through Flask request.values, then validate the input
        using the voluptuous library. Set default values if input
        variables are not given. Returns a dict containg input or
        default values for all parameters """

    s = datamodel().schema()
    try:
        return 1, s(dict(request.values))
    except MultipleInvalid as e:
        return 0, '', str(e)