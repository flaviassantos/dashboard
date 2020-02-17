from flask import Blueprint

bp = Blueprint('machinelearning', __name__)

from app.machinelearning import routes