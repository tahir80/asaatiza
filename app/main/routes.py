from app import create_app, db
from sqlalchemy import exc,asc, desc, and_, or_
import datetime
from app.training import training as tr
from flask import session
import requests
# from app.auth import authentication as at
from flask_login import login_required
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, flash, jsonify # for flash messaging
from app.training.models import TASK, MENTOR, TRAINING, SELF_EFFICACY, POSE_S, ISEL_12

from app.training.forms import CreateNewProject



@tr.route('/')
def home():
    return render_template("TUDelft_questionnaires/q_main_1.html")

@tr.route('/last')
def last():
    return render_template("TUDelft_questionnaires/q_main_10.html")


#################################ADMIN FUNCTIONS###########################################################################
@tr.route('/prolific_admin',  methods=['GET', 'POST'])
# @login_required
def prolific_admin():

    form = CreateNewProject()
    #if data is validate, hten create a new project
    if form.validate_on_submit():
        p_task = TASK(form.title.data, form.Description.data, "ACTIVE")

        db.session.add(p_task)
        db.session.commit()
        flash('task was created Successfully!')
        return redirect(url_for('training.prolific_admin'))
    return render_template("prolific_admin.html", form = form, tasks = TASK.query.order_by(asc(TASK.id)).all())


@tr.route('/changeTaskStatus/<task_id>', methods=['GET', 'POST'])
# @login_required
def changeTaskStatus(task_id):
    task = TASK.query.get(task_id)

    if task.status == "ACTIVE":
        task.status = "DEACTIVE"
    else:
        task.status = "ACTIVE"

    db.session.commit()
    form = CreateNewProject()
    return redirect(url_for('training.prolific_admin'))
    # ,
########################################################################################################################


@tr.route('/mentor_login', methods=['GET', 'POST'])
def mentor_login():
   if request.method == 'GET':
        return render_template("TUDelft_questionnaires/login.html")
   if request.method == 'POST':
       data = request.get_json()

       if MENTOR.query.filter_by(mentor_id = data['mid']).count() > 0:
           dict = {"status": "success"}
           return jsonify(dict)
       else:
           dict = {"status": "failure"}
           return jsonify(dict)
                  # mentor = MENTOR.query.filter_by(mentor_id = data['mid']).first()
       # if not MENTOR.query.filter_by(mentor_id = data['mid']).first():
       #     mentor = MENTOR(data['mid'], datetime.datetime.utcnow())
       #     db.session.add(mentor)
       #     db.session.commit()


       # url = 'training.POSE_S' + "?mentorId=" + request.form['mid']
       # return redirect(url_for( 'training.POSE', mentorId=request.form['mid'], training='no'))




@tr.route('/training')
def training():
    return render_template("training.html")

@tr.route('/self_efficacy', methods=['GET', 'POST'])
def self_efficacy():
    if request.method == 'GET':
        try:
            task = TASK.query.filter_by(status="ACTIVE").first()
        except:
            pass
        if request.args.get("training") == "yes":
            return render_template("TUDelft_questionnaires/self-efficacy0.html")
        else:
            return render_template("TUDelft_questionnaires/self-efficacy.html")

    if request.method == 'POST':
        data = request.get_json()
        mentor = MENTOR.query.filter_by(mentor_id = data['mentorId']).first()
        print(mentor.mentor_id)

        # session['mentorId'] = data['mentorId']
        task = TASK.query.filter_by(status="ACTIVE").first()


        se = SELF_EFFICACY(mentor.id, task.id, data['understand'], data['say_next'], data['Help_client_to_talk'], data['conceptualization'], \
        data['explore'], data['helping_skill'], data['realistic_counseling_goals'], data['focused'], data['intentions'], \
        data['planning'], data['status'], datetime.datetime.utcnow())

        db.session.add(se)

        db.session.commit()

        return jsonify(data)


@tr.route('/setTime', methods=['GET', 'POST'])
def setTime():
    session['start_time'] = datetime.datetime.utcnow()
    return jsonify(123)

@tr.route('/addshortAnswer' , methods=['GET', 'POST'])
def addshortAnswer():
    if request.method == 'POST':
        data = request.get_json()
    task = TASK.query.filter_by(status="ACTIVE").first()
    mentor = MENTOR.query.filter_by(mentor_id = data['mentorId']).first()

    training_data = TRAINING(mentor.id, data['q'], data['ans'], task.id, datetime.datetime.utcnow())

    db.session.add(training_data)
    db.session.flush()

    training_data.start_time = datetime.datetime.min

    # if data['rewardable'] == 'yes':
    #     bonus = BONUS.query.filter(BONUS.w_id==mentor.id).order_by(desc(BONUS.id)).first()
    #     t_bonus = TRAINING_BONUS(bonus.id, training_data.id, 0.1, datetime.datetime.utcnow())
    #     db.session.add(t_bonus)

    db.session.commit()
    return jsonify(123)


@tr.route('/addLongAnswer', methods=['GET', 'POST'])
def addLongAnswer():
    if request.method == 'POST':
        data = request.get_json()
    task = TASK.query.filter_by(status="ACTIVE").first()
    mentor = MENTOR.query.filter_by(mentor_id = data['mentorId']).first()

    training_data = TRAINING(mentor.id, data['q'], data['ans'], task.id, datetime.datetime.utcnow())

    db.session.add(training_data)
    db.session.flush()

    if 'start_time' in session:
        training_data.start_time = session['start_time']
        session.pop('start_time', None)

    # if data['rewardable'] == 'yes':
    #     bonus = BONUS.query.filter(BONUS.w_id==mentor.id).order_by(desc(BONUS.id)).first()
    #     t_bonus = TRAINING_BONUS(bonus.id, training_data.id, 0.1, datetime.datetime.utcnow())
    #     db.session.add(t_bonus)

    db.session.commit()

    print('done adding long answer')
    return jsonify(123)



@tr.route('/POSE_S', methods=['GET', 'POST'])
def POSE():
    if request.method == "GET":
        if request.args.get("training") == "yes":
            return render_template("TUDelft_questionnaires/POSE-S0.html")
        else:
            return render_template("TUDelft_questionnaires/POSE-S.html")

    if request.method == "POST":
        data = request.get_json()
        print(data)
        mentor = MENTOR.query.filter_by(mentor_id = data['mentorId']).first()
        print(mentor.mentor_id)

        # session['mentorId'] = data['mentorId']
        task = TASK.query.filter_by(status="ACTIVE").first()
        print(task.id)

        pose_s = POSE_S(mentor.id, task.id, data['problem_solution'], data['find_way'], data['difficult_problems'], data['optimistic_way'], \
        data['hardly_think_of_positivity'], data['master_difficulties'], data['worry_future'], data['solution_to_a_problem'], \
        data['everything_is_gloomy'], data['beforeafter'], datetime.datetime.utcnow())

        db.session.add(pose_s)
        db.session.commit()

        print(data)
        return jsonify(data)

@tr.route('/ISEL_12', methods=['GET', 'POST'])
def ISEL():
    if request.method == "GET":
        if request.args.get("training") == "yes":
            return render_template("TUDelft_questionnaires/ISEL-120.html")
        else:
            return render_template("TUDelft_questionnaires/ISEL-12.html")

    if request.method == "POST":
            data = request.get_json()
            print(data)
            mentor = MENTOR.query.filter_by(mentor_id = data['mentorId']).first()
            print(mentor.mentor_id)

            # session['mentorId'] = data['mentorId']
            task = TASK.query.filter_by(status="ACTIVE").first()
            print(task.id)

            isel_12 = ISEL_12(mentor.id, task.id, data['item1'], data['item2'], data['item3'], data['item4'], \
            data['item5'], data['item6'], data['item7'], data['item8'], data['item9'], data['item10'], data['item11'], \
            data['item12'], data['beforeafter'], datetime.datetime.utcnow())

            db.session.add(isel_12)
            db.session.commit()

            print(data)
            return jsonify(data)

@tr.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template("TUDelft_questionnaires/thankyou.html")
