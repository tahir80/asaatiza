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
from app.main.models import TASK, WORKER, MESSAGE, SURVEY, TIME_SPENT

from app.main.forms import CreateNewProject, surveys, EditProject


#http://127.0.0.1:5000/bot?context=stress&q=1&c=1&d=2

#https://stackoverflow.com/questions/8551952/how-to-get-last-record

@main.route('/')
def home():
    return render_template("home.html")

@main.route('/bot', methods=['GET', 'POST'])
def bot():
    if request.method == 'POST':
        data = request.get_json()
        print(data['message'])
        # print(type(request.args.get('workerId')))

        message = MESSAGE(data['message'], int(data['workerId']), int(data['task_id']),\
                          session['start_time'], datetime.datetime.utcnow())

        db.session.add(message)
        db.session.commit()
        session.pop('start_time', None)

        return jsonify(123)
    if request.method == 'GET':
        context = request.args.get('context')
        return render_template("bot.html", context=context)


@main.route('/consent', methods=['GET', 'POST'])
def consent():
    if request.method == 'POST' and request.args.get('context') == "stress":
        #get the ID of the task
        task_id = getTaskID(request.args.get('context'), request.args.get('c'), \
                            request.args.get('q'), request.args.get('d'))

        #add worker in the DB
        w_id = addWorker(request.form.get('workerId'))

        return redirect(url_for('main.stress_task', workerId = w_id, task_id = task_id, context=request.args.get('context'), \
        c = request.args.get('c'), q=request.args.get('q'), d=request.args.get('d'), mood = request.form.get('PAM')))

    if request.method == 'POST' and request.args.get('context') == "IR":
        #get the ID of the task
        task_id = getTaskID(request.args.get('context'), request.args.get('c'), \
                            request.args.get('q'), request.args.get('d'))

        #add worker in the DB
        w_id = addWorker(request.form.get('workerId'))
        return redirect(url_for('main.IR_task', workerId = w_id, task_id = task_id, context=request.args.get('context'), \
        c = request.args.get('c'), q=request.args.get('q'), d=request.args.get('d'), mood = request.form.get('PAM')))

    if request.method == 'GET':
        return render_template("consent-form.html")



@main.route('/stress_task', methods=['GET', 'POST'])
def stress_task():
    if request.method == 'POST':
        time_spent = TIME_SPENT("stress_inst", int(request.args.get('workerId')), int(request.args.get('task_id')), \
                                session['start_time'], datetime.datetime.utcnow())
        db.session.add(time_spent)
        db.session.commit()
        session.pop('start_time', None)

        return redirect(url_for('main.bot', workerId = request.args.get('workerId'), task_id = request.args.get('task_id'), context=request.args.get('context'), \
        c = request.args.get('c'), q=request.args.get('q'), d=request.args.get('d'), mood = request.args.get('mood')))
    if request.method == 'GET':
        return render_template("stress-task.html")

@main.route('/IR_task', methods=['GET', 'POST'])
def IR_task():
    if request.method == 'POST':
        time_spent = TIME_SPENT("IR_inst", int(request.args.get('workerId')), int(request.args.get('task_id')), \
                                session['start_time'], datetime.datetime.utcnow())
        db.session.add(time_spent)
        db.session.commit()
        session.pop('start_time', None)

        return redirect(url_for('main.bot', workerId = request.args.get('workerId'), task_id = request.args.get('task_id'), context=request.args.get('context'), \
        c = request.args.get('c'), q=request.args.get('q'), d=request.args.get('d'), mood = request.args.get('mood')))
    if request.method == 'GET':
        return render_template("IR-task.html")

@main.route('/setTime', methods=['GET', 'POST'])
def setTime():
    print("i got you")
    session['start_time'] = datetime.datetime.utcnow()
    return jsonify(123)

@main.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")


@main.route('/exit_surveys', methods=['GET', 'POST'])
def exit_surveys():
    form = surveys()
    if form.validate_on_submit():
        print(request.form['education'])
        s = SURVEY(int(request.args.get('workerId')),\
                   int(request.args.get('task_id')),\
                   request.args.get('mood'),\
               request.form['Perceived_waiting_time'],\
               request.form['cognitive'],\
               request.form['irritation'],\
               request.form['fairness'],\
               request.form['annoyance'],\
               request.form['boredom'],\
               request.form['stress'],\
               request.form['attitude'],\
               request.form['satisfaction'],\
               request.form['feedback'],\
               request.form['suggestion'],\
               request.form['social_o_1'],\
               request.form['social_o_2'],\
               request.form['exp1'],\
               request.form['exp2'],\

               request.form['ati1'],\
               request.form['ati2'],\
               request.form['ati3'],\
               request.form['ati4'],\
               request.form['ati5'],\
               request.form['ati6'],\
               request.form['ati7'],\
               request.form['ati8'],\
               request.form['ati9'],\

               request.form['education'])
        db.session.add(s)
        db.session.commit()

        #store time spent in conv.task in DB
        fillBotTimeSpent(int(request.args.get('workerId')),\
                         int(request.args.get('task_id')),\
                         request.args.get('context'))

        return redirect(url_for('main.thankyou'))


        # form.example.dat
        # print(request.form['social_o_1'], request.form['social_o_1'])

    return render_template("exit-surveys.html", form=form)


@main.route('/prolific_admin',  methods=['GET', 'POST'])
# @login_required
def prolific_admin():

    form = CreateNewProject()

    if form.validate_on_submit():

        t = TASK(form.title.data, form.context.data, form.complexity.data, \
                               form.quality.data, form.delay.data,  form.URL_completion_code.data)
        db.session.add(t)
        db.session.commit()
        flash('task was created Successfully!')
        return redirect(url_for('main.prolific_admin'))

    return render_template("prolific_admin.html", form = form, tasks = TASK.query.order_by(asc(TASK.id)).all(), \
    count = db.session.query(TASK).count())



@main.route('/edit_task/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    print(type(task_id))
    task = TASK.query.get(task_id)
    form = EditProject(obj=task)
    if request.method == 'GET':
        form.title.data = task.title
        form.context.data = task.context
        form.complexity.data = task.complexity
        form.quality.data = task.quality
        form.delay.data = task.delay
        form.url.data  = task.URL_completion_code

    if form.validate_on_submit():
        task.title  = form.title.data
        task.context = form.context.data
        task.complexity = form.complexity.data
        task.quality = form.quality.data
        task.delay = form.delay.data
        task.URL_completion_code = form.url.data
        db.session.add(task)
        db.session.commit()
        flash('Task Edited Successfully')
        return redirect(url_for('main.prolific_admin'))
    return render_template('edit.html', form=form)



####################FUNCTIONS##########################3
def addWorker(worker):
    if not WORKER.query.filter_by(prolific_id = worker).first():
        new_worker = WORKER(worker)
        db.session.add(new_worker)
        db.session.flush()
        w_id = new_worker.id # got the id
        db.session.commit()
        return w_id
    else:
        new_worker = WORKER.query.filter_by(prolific_id = worker).first()
        return new_worker.id


def getTaskID(context, complexity, quality, delay):
    t = TASK.query.filter(and_(TASK.context == context, TASK.complexity == complexity, \
                           TASK.quality == quality, TASK.delay == delay)).first()

    return t.id

#thanks to https://stackoverflow.com/questions/26528300/get-first-and-last-element-with-sqlalchemy
def fillBotTimeSpent(w_id, t_id, context):
    results = MESSAGE.query.filter(and_(MESSAGE.w_id == w_id, MESSAGE.t_id == t_id)).all()
    first = results[0]
    last = results[-1]
    print(first.start_time)
    print(last.end_time)

    if context == "IR":
        stage = "IR_bot_time"
    else:
        stage = "stress_bot_time"


    time_spent = TIME_SPENT(stage, int(request.args.get('workerId')), int(request.args.get('task_id')), \
                            first.start_time, last.end_time)
    db.session.add(time_spent)
    db.session.commit()
