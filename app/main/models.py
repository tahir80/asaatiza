from app import db # we already defined db instance inside app/__init__.py file
import datetime
# from app.auth.models import User

class TASK(db.Model):
    __tablename__ = 'TASK'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    s_start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    s_end_time = db.Column(db.DateTime, nullable = True)
    # c_id = db.Column(db.Integer, db.ForeignKey('CONDITION.id'))
    status = db.Column(db.String(100))

    def __init__(self, title, desc, status):
        self.title = title
        self.desc = desc
        self.status = status

class MENTOR(db.Model):
    __tablename__ = 'MENTOR'
    id = db.Column(db.Integer, primary_key = True)
    mentor_id = db.Column(db.String(100))
    time_stamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    def __init__(self, mentor_id, time_stamp):
        self.mentor_id = mentor_id
        self.time_stamp = time_stamp

class TRAINING(db.Model):
    __tablename__ = 'TRAINING'
    id = db.Column(db.Integer, primary_key = True)
    m_id = db.Column(db.Integer, db.ForeignKey('MENTOR.id'))
    qs = db.Column(db.String(500), nullable = False)
    ans = db.Column(db.String(500), nullable = False)
    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    end_time =db.Column(db.DateTime)
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))

    def __init__(self, m_id, qs, ans, t_id, end_time):
        self.m_id = m_id
        self.qs = qs
        self.ans = ans
        self.t_id = t_id
        # self.start_time = start_time
        self.end_time = end_time


class SELF_EFFICACY(db.Model):

    __tablename__ = 'SELF_EFFICACY'
    id = db.Column(db.Integer, primary_key = True)
    m_id = db.Column(db.Integer, db.ForeignKey('MENTOR.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))
    #survey items
    understand = db.Column(db.String(500), nullable = False)
    say_next = db.Column(db.String(500), nullable = False)
    Help_client_to_talk = db.Column(db.String(500), nullable = False)
    conceptualization = db.Column(db.String(500), nullable = False)
    explore = db.Column(db.String(500), nullable = False)
    helping_skill = db.Column(db.String(500), nullable = False)
    realistic_counseling_goals = db.Column(db.String(500), nullable = False)
    focused = db.Column(db.String(500), nullable = False)
    intentions = db.Column(db.String(500), nullable = False)
    planning = db.Column(db.String(500), nullable = False)
    beforeafter = db.Column(db.String(500), nullable = False)
    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    end_time = db.Column(db.DateTime)

    def __init__(self, m_id, t_id, understand, say_next, Help_client_to_talk, conceptualization, \
    explore, helping_skill, realistic_counseling_goals, focused, intentions, planning, beforeafter, end_time):
        self.m_id = m_id
        self.t_id = t_id
        self.understand = understand
        self.say_next = say_next
        self.Help_client_to_talk = Help_client_to_talk
        self.conceptualization = conceptualization
        self.explore = explore
        self.helping_skill = helping_skill
        self.realistic_counseling_goals = realistic_counseling_goals
        self.focused = focused
        self.intentions = intentions
        self.planning = planning
        self.beforeafter = beforeafter
        self.end_time=end_time

class POSE_S(db.Model):

    __tablename__ = 'POSE_S'
    id = db.Column(db.Integer, primary_key = True)
    m_id = db.Column(db.Integer, db.ForeignKey('MENTOR.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))
    #survey items
    problem_solution = db.Column(db.String(500), nullable = False)
    find_way = db.Column(db.String(500), nullable = False)
    difficult_problems = db.Column(db.String(500), nullable = False)
    optimistic_way = db.Column(db.String(500), nullable = False)
    hardly_think_of_positivity = db.Column(db.String(500), nullable = False)
    master_difficulties = db.Column(db.String(500), nullable = False)
    worry_future = db.Column(db.String(500), nullable = False)
    solution_to_a_problem = db.Column(db.String(500), nullable = False)
    everything_is_gloomy = db.Column(db.String(500), nullable = False)
    beforeafter = db.Column(db.String(500), nullable = False)

    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    end_time = db.Column(db.DateTime)

    def __init__(self, m_id, t_id, problem_solution, find_way, difficult_problems, optimistic_way,
    hardly_think_of_positivity, master_difficulties, worry_future, solution_to_a_problem, everything_is_gloomy, beforeafter, end_time):
        self.m_id = m_id
        self.t_id = t_id
        self.problem_solution = problem_solution
        self.find_way = find_way
        self.difficult_problems = difficult_problems
        self.optimistic_way = optimistic_way
        self.hardly_think_of_positivity = hardly_think_of_positivity
        self.master_difficulties = master_difficulties
        self.worry_future = worry_future
        self.solution_to_a_problem = solution_to_a_problem
        self.everything_is_gloomy = everything_is_gloomy
        self.beforeafter = beforeafter
        self.end_time=end_time


class ISEL_12(db.Model):

    __tablename__ = 'ISEL_12'
    id = db.Column(db.Integer, primary_key = True)
    m_id = db.Column(db.Integer, db.ForeignKey('MENTOR.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))
    #survey items
    item1 = db.Column(db.String(500), nullable = False)
    item2 = db.Column(db.String(500), nullable = False)
    item3 = db.Column(db.String(500), nullable = False)
    item4 = db.Column(db.String(500), nullable = False)
    item5 = db.Column(db.String(500), nullable = False)
    item6 = db.Column(db.String(500), nullable = False)
    item7 = db.Column(db.String(500), nullable = False)
    item8 = db.Column(db.String(500), nullable = False)
    item9 = db.Column(db.String(500), nullable = False)
    item10 = db.Column(db.String(500), nullable = False)
    item11 = db.Column(db.String(500), nullable = False)
    item12 = db.Column(db.String(500), nullable = False)
    beforeafter = db.Column(db.String(500), nullable = False)

    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    end_time = db.Column(db.DateTime)

    def __init__(self, m_id, t_id, item1, item2, item3, item4, item5, item6, item7, item8, item9,item10, item11, item12, beforeafter, end_time):
        self.m_id = m_id
        self.t_id = t_id
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        self.item6 = item6
        self.item7 = item7
        self.item8 = item8
        self.item9 = item9
        self.item10 = item10
        self.item11 = item11
        self.item12 = item12
        self.beforeafter = beforeafter
        self.end_time=end_time
