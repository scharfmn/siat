from flask import Blueprint, flash

demo = Blueprint('demo', __name__, template_folder='templates')

from web.demo import views
