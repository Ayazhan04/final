from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html', user=current_user)