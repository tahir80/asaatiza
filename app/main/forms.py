from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, SelectField, TextAreaField, RadioField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, NumberRange, InputRequired

dropdown_list = [(1,'1'),(2,'1')]
class CreateNewProject(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    context = RadioField('Select the context of this task',
                   choices=[('stress','stress'),('IR','IR')])
    # context = StringField('context', validators=[DataRequired()])
    complexity = RadioField('Select the complexity level',
                   choices=[('1','high'),('0','low')])
    quality = RadioField('Select the quality level',
                       choices=[('1','high'),('0','low')])

    delay = RadioField('Select the delay level',
                       choices=[('2','2-sec'),('4','4-sec'),('8','8-sec'),('12','12-sec'), ('16','16-sec')])

    URL_completion_code = StringField('URL Completion Code', validators=[InputRequired()])
    # quality = FloatField('quality', validators=[DataRequired()])
    # delay = StringField('delay', validators=[DataRequired()])
    submit = SubmitField("create a new task")
    # deactivate = SubmitField('DEACTIVATE THIS TASK')

class EditProject(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    context = RadioField('Select the context of this task',
                   choices=[('stress','stress'),('IR','IR')])
    # context = StringField('context', validators=[DataRequired()])
    complexity = RadioField('Select the complexity level',
                   choices=[('1','high'),('0','low')])
    quality = RadioField('Select the quality level',
                       choices=[('1','high'),('0','low')])

    delay = RadioField('Select the delay level',
                       choices=[('2','2-sec'),('4','4-sec'),('8','8-sec'),('12','12-sec'), ('16','16-sec')])

    url = StringField('URL Completion Code', validators=[InputRequired()])
    # quality = FloatField('quality', validators=[DataRequired()])
    # delay = StringField('delay', validators=[DataRequired()])
    submit = SubmitField("Update")


class surveys(FlaskForm):
    Perceived_waiting_time = IntegerField('(1) Please indicate how long you perceive the response delay of the crowd-powered conversational system you just experienced (in seconds)',
                                        validators=[InputRequired(), NumberRange(min=1, max=50)])

    cognitive = RadioField('How long did you perceive the response delay of the crowd-powered conversational system you just experienced?',
               choices=[('1','Very  Short'),('2','Short'), ('3','Normal'),('4','Long'), ('5', 'Very long')])

    irritation  = RadioField('Irritation',
                  choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    fairness  = RadioField('fairness',
                      choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    annoyance  = RadioField('annoyance',
                choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    boredom  = RadioField('boredom',
                    choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    stress  = RadioField('stress',
                    choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    attitude  = RadioField('Please indicate your attitude towards the response delay of the crowd-powered conversational system you just experienced (choose one):',
                   choices=[('1','Intolerable delay'),('2','Excessive but still tolerable delay'), ('3','Acceptable delay'),('4','Not significant delay')])

    satisfaction  = RadioField('Indicate your overall satisfaction with the service provided by crowd-powered conversational system ',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6'), ('7','7'),('8','8'), ('9','9'), ('10','10')])

    feedback     = TextAreaField('Please provide brief feedback about your feelings for the response delays you just experienced with the system.', validators=[InputRequired()])

    suggestion     = TextAreaField('If you think the delay was long enough, then please suggest an idea for the design of CPCS for handling long delays?')

    social_o_1 =  RadioField("I think 'small talk' with a chatbot is enjoyable ",
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    social_o_2 =  RadioField("I like chatting casually with a chatbot",
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])


    exp1 =  RadioField("I am familiar with chatbot technologies ",
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    exp2 =  RadioField("I use chatbots frequently. ",
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    ati1  = RadioField('I like to occupy myself in greater detail with technical systems.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    ati2  = RadioField('I like testing the functions of new technical systems.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    ati3  = RadioField('I predominantly deal with technical systems because I have to.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    ati4  = RadioField('When I have a new technical system in front of me, I try it out intensively.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    ati5  = RadioField('I enjoy spending time becoming acquainted with a new technical system.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    ati6  = RadioField('It is enough for me that a technical system works; I don’t care how or why.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    ati7  = RadioField('I try to understand how a technical system exactly works.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    ati8  = RadioField('It is enough for me to know the basic functions of a technical system.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    ati9  = RadioField('I try to make full use of the capabilities of a technical system.',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6')])

    education = SelectField('What’s your highest level of education?', [DataRequired()],
        choices=[
            ('No formal education', ' No formal education'),
            ('High school diploma', 'High school diploma'),
            ('College degree', 'College degree'),
            ('Vocational training', 'Vocational training'),
            ('Bachelor’s degree', 'Bachelor’s degree'),
            ('Master’s degree', 'Master’s degree'),
            ('Professional degree', 'Professional degree'),
            ('Doctorate degree', 'Doctorate degree'),
            ('Other', 'Other'),
        ]
    )

    submit = SubmitField('Submit')
