from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, SelectField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

dropdown_list = [(1,'1'),(2,'1')]
class CreateNewProject(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    Description = TextAreaField(validators=[DataRequired()])
    # Description = StringField('Description', validators=[DataRequired()])
    # no_of_workers = IntegerField('Number of Workers', validators=[DataRequired()])
    # Fix_reward = FloatField('Fixed Reward', validators=[DataRequired()])
    # completion_code = StringField('URL completion code', validators=[DataRequired()])
    # c_id = IntegerField('condition', validators=[DataRequired()])
    # conditions = SelectField('Conditions', choices=dropdown_list, default=1)
    create_button = SubmitField('CREATE A TASK')
    # deactivate = SubmitField('DEACTIVATE THIS TASK')
