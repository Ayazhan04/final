from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        telephone = request.form.get('telephone')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='success')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(str(telephone)) > 11:
            flash('Password must be 11 characters.', category='error')
        else:
            new_user = User(email=email, name=name, telephone=telephone)
            db.session.add(new_user)
            db.session.commit()

            flash('Account created!', category='success')
            return redirect(url_for('views.index'))

    return render_template("signup.html", user=current_user)