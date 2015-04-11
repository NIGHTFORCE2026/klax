# import blueprint 
from flask import Blueprint 

# create a blueprint instance
auth = Blueprint('auth', __name__)

# associate blueprint with package's view functions
from . import views
