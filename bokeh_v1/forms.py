from flask_wtf import FlaskForm
import numpy as np
from wtforms import StringField, SelectMultipleField, IntegerField, FloatField, SubmitField, validators, ValidationError
from wtforms.widgets import ListWidget, CheckboxInput


roll_set_dict = {'17d070060': 0, '16d070049': 0, '17d070051': 0, '183074022': 0, '16d070058': 0, '15d070004': 1, '16d070026': 1, '193076001': 1, 'rk': 1, '194076011': 1, '16d070024': 2, '15d070008': 2, '15d070051': 2, '16d070016': 2, '173074016': 2, 'yogesh': 3, '183074002': 3, '193071001': 3, '15d070016': 3, '170070049': 3, '16d070023': 4, '193070021': 4, '193074008': 4, '183070028': 4, '16d070028': 4, '19v972009': 5, '17d070054': 5, '183074009': 5, '163079019': 5, '194178002': 5, '16d070053': 6, '18i170013': 6, '173074017': 6, '17d070039': 6, '170070048': 6, '17d070061': 7, '16d070062': 7, 'karan': 7, '16d070061': 7, '170070041': 7, '15d070032': 8, '160070049': 8, '16d070030': 8, '16d070059': 8, '17d070058': 8, '194366003': 8, 'naren': 8}

admin_roll_list = ['naren', 'rk', 'yogesh', 'karan']

###############################################################################
def roll_check(form, field):
    #if field.data not in roll_list:
    if roll_set_dict.get(field.data.lower())==None:
        raise ValidationError('Enter the Roll number enrolled in EE765')

def req_check(form, field):
    req_raw = field.data
    sam_sum = 500
    dur_sum = 1000
    req_stripspc = req_raw.strip(' ')
    req_stripcol = req_stripspc.strip(';')
    req_split    = req_stripcol.split(';')
    req_split_stripsp = [x.strip(' ') for x in req_split]
    req_split_stripr = [x.rstrip(')') for x in req_split_stripsp]
    req_split_strip = [x.lstrip('(') for x in req_split_stripr]
    siz = 4
    result = []
    for req_single in req_split_strip:
        req_single_strip = req_single.strip(' ')
        req_single_split = req_single_strip.split(',')
        if (len(req_single_split)!=siz):
            raise ValidationError('Consistent size issue')
        try:
            single_exp = [int(x.strip(' ')) for x in req_single_split]
            for x in single_exp:
                if x<0:
                    raise ValidationError('Negatives not allowed')
            result.append(single_exp)
        except:
            raise ValidationError('Ensure proper parameter values (Only positive integers allowed)')
        print(result)
    sample_sum = (np.array([x[0] for x in result])).sum()
    print(f'Sample sum is {sample_sum}')
    duration_sum = (np.array([x[1] for x in result])).sum()
    print(f'Duration sum is {duration_sum}')
    if (sample_sum>sam_sum):
        print ("Sample sum")
        raise ValidationError(f'Total sample number should be <= {sam_sum}')
    if (duration_sum>dur_sum):
        print ("Duration sum")
        raise ValidationError(f'Total chamber time should be <={dur_sum}')

def admin_roll_check(form, field):
    if field.data not in admin_roll_list:
        raise ValidationError('Enter admin ID only, not for students')

###############################################################################

class Assn2Form(FlaskForm):
    """Form to take roll number and Data Points"""
    rollno = StringField('Roll number', [validators.Required("Please enter your roll number."), roll_check])
    #option = SelectMultipleField('Files to download', [validators.Required(message='Chose at least one file to download')], choices=[('1', 'Problem1'), ('2', 'Problem2'), ('3','Problem3')])
    submit1 = SubmitField('Download for problem1')
    submit2 = SubmitField('Download for problem2')
    submit3 = SubmitField('Download for problem3')

###############################################################################
class ProjectForm(FlaskForm):
    """Form to take roll number and Input String"""
    group = IntegerField('Group number', [validators.Required("Please enter your group number"), validators.NumberRange(min=1, max=24)])
    requirement = StringField('Experiment Plan', [validators.Required("Please fill the experiment plan"), validators.length(max=1000), req_check])
    submit = SubmitField('Download')
###############################################################################
class AdminInputForm(FlaskForm):
    """Form to take roll number and Data Points"""
    rollno = StringField('Roll number', [validators.Required("Please enter your roll number."), admin_roll_check])
    shape = FloatField('Shape Parameter', [validators.Required("Please enter shape param.")])
    scale = FloatField('Scale Parameter', [validators.Required("Please enter scale param.")]) 
    points = IntegerField('Data Points (10-100000)', [validators.Required("Please enter a number between 10 and 100000"), validators.NumberRange(min=10, max=100000)])
    seed = IntegerField('Seed', default=0)
    noise_level = FloatField('Noise Addition', default = 0)
    submit = SubmitField('Download')
