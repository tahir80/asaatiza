from app import create_app, db
from sqlalchemy import exc,asc, desc, and_, or_
import datetime
from app.main import main
from flask import session
import requests
# from app.auth import authentication as at
from flask_login import login_required
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, flash, jsonify # for flash messaging
# from app.training.models import TASK, MENTOR, TRAINING, SELF_EFFICACY, POSE_S, ISEL_12

from app.main.forms import CreateNewProject


#http://127.0.0.1:5000/bot?context=stress&q=1&c=1&d=2
@main.route('/bot')
def bot():
    context = request.args.get('context')
    return render_template("bot.html", context=context)

@main.route('/prolific_admin',  methods=['GET', 'POST'])
# @login_required
def prolific_admin():

    form = CreateNewProject()
    #if data is validate, hten create a new project
    if form.validate_on_submit():
        p_task = TASK(form.title.data, form.Description.data, "ACTIVE")

        db.session.add(p_task)
        db.session.commit()
        flash('task was created Successfully!')
        return redirect(url_for('main.prolific_admin'))
    return render_template("prolific_admin.html", form = form, tasks = TASK.query.order_by(asc(TASK.id)).all())
