# ----------------------------------------------------
# PACKAGE BLUEPRINT: main
# ----------------------------------------------------
from flask import Blueprint

main = Blueprint('main', __name__)

# register controllers with the blueprint 
from . import views, errors
