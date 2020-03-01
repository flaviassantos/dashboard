from flask import render_template, jsonify
from app.machinelearning import bp
from app.machinelearning.datamodel import datamodel
from app.machinelearning.predict import predict


@bp.route('/machine_learning_prediction')
def prediction():
    dm = datamodel()
    return render_template('machinelearning/predict.html',
                           options=dm.description(),
                           models=dm.get_models())


@bp.route('/script.js', methods=['GET'])
def serve_script():
    return bp.send_static_file('script.js')


@bp.route('/predict', methods=['GET', 'POST'])
def query_predict_default():
    return jsonify(predict('grad_boosting_regressor'))


@bp.route('/predict/<string:model_name>', methods=['GET', 'POST'])
def query_predict(model_name):
    return jsonify(predict(model_name))