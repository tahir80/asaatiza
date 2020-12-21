from app import db # we already defined db instance inside app/__init__.py file
import datetime
# from app.auth.models import User

class TASK(db.Model):
    __tablename__ = 'TASK'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    context = db.Column(db.String(500), nullable = False)
    complexity = db.Column(db.String(500), nullable = False)
    quality = db.Column(db.String(500), nullable = False)
    delay = db.Column(db.String(500), nullable = False)
    URL_completion_code = db.Column(db.String(500))
    time_stamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    def __init__(self, title, context, complexity, quality, delay, URL_completion_code):
        self.title = title
        self.context = context
        self.complexity = complexity
        self.quality = quality
        self.delay = delay
        self.URL_completion_code = URL_completion_code

class WORKER(db.Model):
    __tablename__ = 'WORKER'
    id = db.Column(db.Integer, primary_key = True)
    prolific_id = db.Column(db.String(100))
    time_stamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    def __init__(self, prolific_id):
        self.prolific_id = prolific_id

class SURVEY(db.Model):

    __tablename__ = 'SURVEY'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('WORKER.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))
    #survey items
    mood = db.Column(db.String(500), nullable = False)
    PWT = db.Column(db.String(500), nullable = False)
    cognitive = db.Column(db.String(500), nullable = False)
    affective_irritation = db.Column(db.String(500), nullable = False)
    affective_fairness = db.Column(db.String(500), nullable = False)
    affective_annoyance = db.Column(db.String(500), nullable = False)
    affective_boredom = db.Column(db.String(500), nullable = False)
    affective_stress = db.Column(db.String(500), nullable = False)
    attitude  = db.Column(db.String(500), nullable = False)
    satisfaction  = db.Column(db.String(500), nullable = False)
    feedback  = db.Column(db.String(500), nullable = False)
    suggestion = db.Column(db.String(500))
    social_o_1  = db.Column(db.String(500), nullable = False)
    social_o_2  = db.Column(db.String(500), nullable = False)
    exp1  = db.Column(db.String(500), nullable = False) # experience with chatbot
    exp2  = db.Column(db.String(500), nullable = False)
    ati1  = db.Column(db.String(500), nullable = False)
    ati2 = db.Column(db.String(500), nullable = False)
    ati3 = db.Column(db.String(500), nullable = False)
    ati4 = db.Column(db.String(500), nullable = False)
    ati5  = db.Column(db.String(500), nullable = False)
    ati6 = db.Column(db.String(500), nullable = False)
    ati7 = db.Column(db.String(500), nullable = False)
    ati8 = db.Column(db.String(500), nullable = False)
    ati9 = db.Column(db.String(500), nullable = False)
    education = db.Column(db.String(500), nullable = False)

    time_stamp = db.Column(db.DateTime, default = datetime.datetime.utcnow)

    def __init__(self, w_id, t_id, mood, PWT, cognitive, affective_irritation, affective_fairness, \
    affective_annoyance, affective_boredom, affective_stress, attitude, satisfaction, feedback, suggestion, \
    social_o_1, social_o_2, exp1, exp2, ati1, ati2, ati3, ati4, ati5, ati6, ati7, ati8, ati9, education):
        self.w_id = w_id
        self.t_id = t_id
        self.mood = mood
        self.PWT = PWT
        self.cognitive = cognitive
        self.affective_irritation = affective_irritation
        self.affective_fairness = affective_fairness
        self.affective_annoyance = affective_annoyance
        self.affective_boredom = affective_boredom
        self.affective_stress = affective_stress
        self.attitude = attitude
        self.satisfaction = satisfaction
        self.feedback = feedback
        self.suggestion = suggestion
        self.social_o_1 = social_o_1
        self.social_o_2 = social_o_2
        self.exp1 = exp1
        self.exp2 = exp2
        self.ati1 = ati1
        self.ati2 = ati2
        self.ati3 = ati3
        self.ati4 = ati4
        self.ati5 = ati5
        self.ati6 = ati6
        self.ati7 = ati7
        self.ati8 = ati8
        self.ati9 = ati9
        self.education = education

class MESSAGE(db.Model):

    __tablename__ = 'MESSAGE'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('WORKER.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))

    user_utterance = db.Column(db.String(500), nullable = False)
    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    end_time =db.Column(db.DateTime)

    def __init__(self, user_utterance, w_id, t_id, start_time, end_time):
        self.user_utterance = user_utterance
        self.w_id = w_id
        self.t_id = t_id
        self.end_time = end_time
        self.start_time = start_time

class TIME_SPENT(db.Model):
    __tablename__ = 'TIME_SPENT'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('WORKER.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))

    stage = db.Column(db.String(500), nullable = False)
    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    end_time =db.Column(db.DateTime)

    def __init__(self, stage, w_id, t_id, start_time, end_time):
        self.stage = stage
        self.w_id = w_id
        self.t_id = t_id
        self.end_time = end_time
        self.start_time = start_time
