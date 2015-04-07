# ROUTE BLUEPRINT
from flask import Blueprint

# p1 blueprint name, p2 module or package where blueprint is located
main = Blueprint('main', __name__)

# associate routes with the blueprint via an import 
from . import views, errors

# register the blueprint with app factory, views, errors
