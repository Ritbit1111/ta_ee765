import time
from flask import Flask, render_template, redirect, url_for, Response, send_file
import pandas as pd
import numpy as np
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, FloatField, SubmitField, validators, ValidationError
#import forms
from bokeh.embed import server_document
from bokeh.server.server import Server
from bokeh.themes import Theme
from tornado.ioloop import IOLoop

roll_set_dict = {'17d070060': 0, '16d070049': 0, '17d070051': 0, '183074022': 0, '16d070058': 0, '15d070004': 1, '16d070026': 1, '193076001': 1, 'rk': 1, '194076011': 1, '16d070024': 2, '15d070008': 2, '15d070051': 2, '16d070016': 2, '173074016': 2, 'yogesh': 3, '183074002': 3, '193071001': 3, '15d070016': 3, '170070049': 3, '16d070023': 4, '193070021': 4, '193074008': 4, '183070028': 4, '16d070028': 4, '19v972009': 5, '17d070054': 5, '183074009': 5, '163079019': 5, '194178002': 5, '16d070053': 6, '18i170013': 6, '173074017': 6, '17d070039': 6, '170070048': 6, '17d070061': 7, '16d070062': 7, 'karan': 7, '16d070061': 7, '170070041': 7, '15d070032': 8, '160070049': 8, '16d070030': 8, '16d070059': 8, '17d070058': 8, '194366003': 8, 'naren': 8}

set_list = {0:[(1,800),(2,500),(0.5,100)],
            1:[(1,900),(3,400),(0.5,200)],
            2:[(1,1000),(2,300),(0.5,500)],
            3:[(1,700),(3,200),(0.7,400)],
            4:[(1,1100),(2,100),(0.7,300)],
            5:[(1,1200),(3,200),(0.5,400)],
            6:[(1,600),(2,300),(0.7,100)],
            7:[(1,1300),(3,400),(0.7,200)],
            8:[(1,1400),(2,500),(0.5,300)],
            }
admin_roll_list = ['naren', 'rk', 'yogesh', 'karan']

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '45df45653df23224'

def modify_doc(doc):
    layout = plot.plot(400, 400)
    doc.add_root(layout)
    #doc.theme = Theme(filename="theme.yaml")

@app.route("/home", methods = ['POST', 'GET'])
@app.route('/', methods=['GET', 'POST'])
def bkapp_page():
    script = server_document('http://10.107.32.38:5006/bkapp')
    return render_template("home.html",title='EE765_distributions', script=script)


@app.route('/assn2', methods=['GET', 'POST'])
def assn2():
    form = forms.Assn2Form()
    #prob = assn2.assn2_probems()
    if form.validate_on_submit():
        roll = form.rollno.data.lower()
        if form.submit1.data==True:
            csv, problem = assn2_module.get_problem1_csv(roll)
        elif form.submit2.data==True:
            csv, problem  = assn2_module.get_problem2_csv(roll)
        elif form.submit3.data==True:
            csv, problem  = assn2_module.get_problem3_csv(roll)
        else:
            return render_template("assn2.html", title="Assignment 2 EE765", form=form) 
        timestr = time.strftime("%m-%d@%H.%M.%S")
        filename = f'{problem}_{roll}_{timestr}'
        return Response( csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=%s.csv"%filename})
    return render_template("assn2.html", title="Assignment 2 EE765", form=form) 


@app.route('/assn3', methods=['GET', 'POST'])
def assn3():
    form = forms.Assn2Form()
    #prob = assn2.assn2_probems()
    if form.validate_on_submit():
        roll = form.rollno.data.lower()
        if form.submit1.data==True:
            csv, problem = assn3_module.get_problem1_csv(roll)
        elif form.submit2.data==True:
            csv, problem  = assn3_module.get_problem2_csv(roll)
        elif form.submit3.data==True:
            csv, problem  = assn3_module.get_problem3_csv(roll)
        else:
            return render_template("assn3.html", title="Assignment 3 EE765", form=form) 
        timestr = time.strftime("%m-%d@%H.%M.%S")
        filename = f'{problem}_{roll}_{timestr}'
        return Response( csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=%s.csv"%filename})
    return render_template("assn3.html", title="Assignment 3 EE765", form=form) 

@app.route('/project', methods=['GET', 'POST'])
def proj():
    form = forms.ProjectForm()
    if form.validate_on_submit():
        group = form.group.data
        req_raw = form.requirement.data
        req_stripspc = req_raw.strip(' ')
        req_stripcol = req_stripspc.strip(';')
        req_split    = req_stripcol.split(';')
        req_split_stripsp = [x.strip(' ') for x in req_split]
        req_split_stripr = [x.rstrip(')') for x in req_split_stripsp]
        req_split_strip = [x.lstrip('(') for x in req_split_stripr]
        result = []
        for req_single in req_split_strip:
            req_single_strip = req_single.strip(' ')
            req_single_split = req_single_strip.split(',')
            result.append([int(x.strip(' ')) for x in req_single_split])
        csv = proj_module.get_data(group, result)
        timestr = time.strftime("%m-%d@%H.%M.%S")
        filename = f'{group}_{timestr}'
        return Response( csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=%s.csv"%filename})
    return render_template("project.html", title="Project EE765", form=form) 

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    form = forms.AdminInputForm()
    if form.validate_on_submit():
        roll = form.rollno.data
        points = form.points.data
        scale = form.scale.data
        seed = form.seed.data
        shape = form.shape.data
        noise_level = form.noise_level.data
        np.random.seed(seed)
        s = scale * np.random.weibull(shape, points)
        s_with_noise = np.round(s + np.random.normal(0, noise_level, points), 2)
        df = pd.DataFrame({'Values':s_with_noise})
        df2 = df.sort_values('Values')
        df2['Sample#'] = df2.index + 1
        df2.index = range(points)
        df2.index.name = 'Index' 
        df2 = df2[['Sample#', 'Values']]
        csv = df2.to_csv()
        timestr = time.strftime("%m-%d@%H.%M.%S")
        filename = f'data_{roll}_{timestr}'
        return Response( csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=%s.csv"%filename})

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
