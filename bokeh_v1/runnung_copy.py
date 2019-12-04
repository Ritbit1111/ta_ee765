import time
from flask import Flask, render_template, redirect, url_for, Response, send_file
import pandas as pd
import numpy as np
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, FloatField, SubmitField, validators, ValidationError

from bokeh.embed import server_document
from bokeh.server.server import Server
from bokeh.themes import Theme
from tornado.ioloop import IOLoop

roll_list = ['rk', 'naren', 'yogesh', 'karan', '154076022','15D070032','15D070051', '15D070033' ,'160070049','160100059','16D070023','16D070024','16D070026','16D070030','16D070049','16D070059','16D070062','170070002','170070016','170070041','173074002','173074016','173074017','17D070020','17D070022','17D070039','17D070051','17D070054','17D070058','17D070060','17D070061','17D070063','183074002','183074009','183074017','183074018','183074022','183170012','183170021','184073001','184073004','18I170013','193070024','193070076','193076001','194076011','194366003','16D070027','16D070029']

admin_roll_list = ['naren', 'rk', 'yogesh', 'karan']

def roll_check(form, field):
    if field.data not in roll_list:
        raise ValidationError('Enter the Roll number enrolled in EE765')

def admin_roll_check(form, field):
    if field.data not in admin_roll_list:
        raise ValidationError('Enter admin ID only, not for students')
class InputForm(FlaskForm):
    """Form to take roll number and Data Points"""
    rollno = StringField('Roll number', [validators.Required("Please enter your roll number."), roll_check])
    points = IntegerField('Data Points (10-1000)', [validators.Required("Please enter a number between 10 and 1000"), validators.NumberRange(min=10, max=1000)])
    submit = SubmitField('Download')

class AdminInputForm(FlaskForm):
    """Form to take roll number and Data Points"""
    rollno = StringField('Roll number', [validators.Required("Please enter your roll number."), admin_roll_check])
    shape = FloatField('Shape Parameter', [validators.Required("Please enter shape param.")])
    scale = FloatField('Scale Parameter', [validators.Required("Please enter scale param.")]) 
    points = IntegerField('Data Points (10-100000)', [validators.Required("Please enter a number between 10 and 100000"), validators.NumberRange(min=10, max=100000)])
    submit = SubmitField('Download')

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '45df45653df23224'

def modify_doc(doc):

    layout = plot.plot(400, 400)
    doc.add_root(layout)
#
    # doc.theme = Theme(filename="theme.yaml")

@app.route("/home", methods = ['POST', 'GET'])
@app.route('/', methods=['GET', 'POST'])
def bkapp_page():
    form = InputForm()
    #form = forms.InputForm()
    if form.validate_on_submit():
        roll = form.rollno.data
        points = form.points.data
        if roll in roll_list:
            s = np.random.weibull(0.5,points)
            df = pd.DataFrame({'Values':s})
            df.index.name = 'Index' 
            csv = df.to_csv()
            timestr = time.strftime("%m-%d@%H.%M.%S")
            filename = f'data_{roll}_{timestr}'
            return Response( csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=%s.csv"%filename})
        else:
            return render_template("home.html",title='EE765', form=form)

    #script = server_document('http://www.ee.iitb.ac.in/EE765_2019/bkapp')
    script = server_document('http://10.107.32.38:5006/bkapp')
    return render_template("home.html",title='EE765', form=form, script=script)

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    form = AdminInputForm()
    if form.validate_on_submit():
        roll = form.rollno.data
        points = form.points.data
        scale = form.scale.data
        shape = form.shape.data
        if roll in admin_roll_list:
            s = scale * np.random.weibull(shape, points)
            s.sort()
            df = pd.DataFrame({'Values':s})
            df.index.name = 'Index' 
            csv = df.to_csv()
            timestr = time.strftime("%m-%d@%H.%M.%S")
            filename = f'data_{roll}_{timestr}'
            return Response( csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=%s.csv"%filename})
        else:
            return render_template("admin.html",title='EE765_admin', form=form)

    return render_template("admin.html",title='EE765_admin', form=form)

def bk_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server({'/bkapp': modify_doc}, io_loop=IOLoop(), allow_websocket_origin=["10.107.32.38"])
    server.start()
    server.io_loop.start()

from threading import Thread
Thread(target=bk_worker).start()

if __name__ == '__main__':
    app.run()

