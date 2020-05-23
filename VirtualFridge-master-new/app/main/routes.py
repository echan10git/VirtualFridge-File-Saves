from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import db
from app.main.forms import EditProfileForm, EmptyForm
from app.models import User
from app.main import bp

@bp.route("/")
def landing_page():
    return render_template('landing_page.html', title='Landing Page')

@bp.route("/home")
@login_required
def home():
    return render_template('home.html', title='Home')

@bp.route("/myfridge")
def myfridge():
    return render_template('myfridge.html', title='My Fridge')

@bp.route("/search")
def search():
    return render_template('search.html', title='Search')

@bp.route("/submit")
def submit():
    return render_template('submit.html', title='Submit')

@bp.route("/popular")
def popular():
    return render_template('popular.html', title='Popular')

@bp.route("/help")
def help():
    return render_template('help.html', title='Help')

@bp.route('/edit_profile', methods = ['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Changes successfully made!')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)

@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


