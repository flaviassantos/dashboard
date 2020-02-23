# @bp.route('/predict', methods=['POST', 'GET'])
# def predict():
#     '''
#     For rendering ML results on HTML GUI.
#     '''
#     model = run_model()  # pickle.load(open('model.pkl', 'rb'))
#
#     int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#
#     output = round(prediction[0], 2)
#
#     return render_template('index.html', title='Prediction', prediction_text=f'Employee Salary should be $ {output}')
