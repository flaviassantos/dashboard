import numpy as np
from flask import render_template, request
import pickle
from app.machinelearning import bp

model = pickle.load(open('model.pkl', 'rb'))


@bp.route('/predictions', methods=['GET', 'POST'])
def predict():
    '''
    For rendering ML results on HTML GUI.
    '''
    form = PredictionForm()
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('prediction.html', prediction_text='Employee Salary should be $ {}'.format(output))
